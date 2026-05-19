from country import Country



data = {
    "name": {"common": "Argentina"},
    "capital": ["Buenos Aires"],
    "population": 45376763,
    "area": 2780400.0,
    "region": "Americas"
}

pais = Country(data)

print(pais.nombre)
print(pais.capital)
print(pais.poblacion)
print(pais.area)
print(pais.region)