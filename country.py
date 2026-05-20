import requests
import time
from requests.exceptions import HTTPError, ConnectionError, Timeout
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE= "https://restcountries.com/v3.1"

class Country: 
    def __init__(self, data: dict)-> None:
        self.nombre=data["name"]["common"]
        self.capital= data.get("capital",["--"])[0]
        self.poblacion= data.get("population",0)
        self.area= data.get("area",0)
        self.region = data.get("region", "--")
    
    def __str__(self)-> str:
        return(
            f"{self.nombre} ({self.region})\n"
            f"Capital: {self.capital}\n"
            f"Poblacion: {self.poblacion:,}\n"
            f"Area: {self.area:,.2f}\n"
            f"Densidad: {self.density():.2f} hab/km^2"
            
        )
    def density(self)-> float:
        return self.poblacion/ self.area if self.area else 0
    
    def comparar(self, otros: list) -> None:
        todos = [self] + otros
        mayor_poblacion = max(todos, key=lambda p: p.poblacion)
        mayor_area = max(todos, key=lambda p: p.area)
        mayor_densidad = max(todos, key=lambda p: p.density())

        print()
        print("─" * 78)
        print(f"{'PAIS':^15} {'POBLACION':^15} {'AREA':^15} {'DENSIDAD':^15}")
        print("─" * 78)

        for p in todos:
            print(f"{p.nombre:^15} {p.poblacion:^15,} {p.area:^15,.2f} {p.density():^15.2f} hab/km^2")

        print("─" * 78)
        print(f"Mayor poblacion: {mayor_poblacion.nombre}")
        print(f"Mayor area: {mayor_area.nombre}")
        print(f"Mayor densidad: {mayor_densidad.nombre}")
        
class CountryAPI:
    def by_nombre(self, nombre:str) -> Country | None:
        url= f"{BASE}/name/{nombre}?fullText=true"
        try:
            
            r=requests.get(url,timeout=5)
            r.raise_for_status()
            return Country(r.json()[0])
        except Timeout:
            print(f"Demasiado tiempo de espera para la API al buscar {nombre}")
        except ConnectionError:
            print(f"No hay acceso a internet al buscar {nombre}")
        except HTTPError as e:
            print(f"Error {e.response.status_code} con {nombre}")
        return None
    
    def by_region(self, region:str)-> list[Country]:
        url= f"{BASE}/region/{region}"
        
        r=requests.get(url, timeout=5)
        r.raise_for_status()    
        return [Country(p) for p in r.json()]
    
    
    def by_nombres_concurrencia(self, nombres: list) -> list[Country]:
        inicio = time.perf_counter()
        with ThreadPoolExecutor(max_workers=6) as executor:
            futuros = {executor.submit(self.by_nombre, nombre): nombre for nombre in nombres}
            paises = []
            for futuro in as_completed(futuros):
                pais = futuro.result()
                if pais is not None:
                    paises.append(pais)

        fin = time.perf_counter()
        print(f"Demora en concurrencia: {fin - inicio:.4f} segundos")
        return paises

        
    