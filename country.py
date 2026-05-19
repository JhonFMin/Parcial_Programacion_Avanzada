import requests

from requests.exceptions import HTTPError, ConnectionError, Timeout

api= "https://restcountries.com/v3.1"

class Country: 
    def __init__(self, data):
        self.nombre=data["name"]["common"]
        self.capital= data.get("capital",["--"])[0]
        self.poblacion= data.get("population",0)
        self.area= data.get("area",0)
        self.region = data.get("region", "--")
    

class CountryAPI:
    pass

