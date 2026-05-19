import requests

from requests.exceptions import HTTPError, ConnectionError, Timeout

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
            f"Densidad: {self.density():.2f}hab/km^2"
            
        )
    def density(self)-> float:
        return self.poblacion/ self.area if self.area else 0
    
    

class CountryAPI:
    def by_name(self, nombre:str) -> Country | None:
        url= f"{api}/name/{nombre}"
        try:
            r=requests.get(url,timeout=5)
            r.raise_for_status()
            return Country(r.json()[0])
        except Timeout:
            print("Demaciado tiempo de espera para la API")
        except ConnectionError:
            print("No hay acceso a internet")
        except HTTPError as e:
            print(f"Error {e.response.status_code}: no encontrado")
        return None
    
    def by_region(self, region:str)-> list[Country]:
        url= f"{api}/region/{region}"
        r=requests.get(url, timeout=5)
        r.raise_for_status()
        return [Country(p) for p in r.json()]
    