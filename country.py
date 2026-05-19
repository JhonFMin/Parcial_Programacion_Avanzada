import requests

from requests.exceptions import HTTPError, ConnectionError, Timeout
from concurrent.futures import ThreadPoolExecutor

api= "https://restcountries.com/v3.1"

class Country: 
    def __init__(self, data: dict):
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
            f"Area: {self.area: ,.2f}\n"
            f"Densidad: {self.density():.2f} hab/km^2"
            
        )
    def density(self)-> float:
        return self.poblacion/ self.area if self.area else 0
    
    def comparar(self, otros:list) ->None:
        todos=[self]+ otros
        mayor_poblacion= max(todos,key=lambda p: p.poblacion)
        mayor_area= max(todos, key=lambda p: p.area)
        mayor_densidad= max(todos, key=lambda p: p.density())
        print ("Pais - Poblacion - Area - Densidad")
        for p in todos:
            print(
                f"{p.nombre} - {p.poblacion} - {p.area} - {p.density():.2f} hab/km^2"
            )
        print("\n─────────────────────────────────────────────────")
        print(f"Mayor población : {mayor_poblacion.nombre}")
        print(f"Mayor área      : {mayor_area.nombre}")
        print(f"Mayor densidad  : {mayor_densidad.nombre}")
class CountryAPI:
    def by_nombre(self, nombre:str) -> Country | None:
        url= f"{api}/name/{nombre}?fullText=true"
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
        url= f"{api}/region/{region}"
        r=requests.get(url, timeout=5)
        r.raise_for_status()    
        return [Country(p) for p in r.json()]
    
    def by_nombres(self,nombres:list):
        with ThreadPoolExecutor() as executor:
            paises= list(executor.map(self.by_nombre,nombres))
        return [p for p in paises if p is not None]
    
    