from country import CountryAPI

api = CountryAPI()

nombres = ["spain", "denmark", "uzbekistan"]

paises = api.by_names(nombres)

for pais in paises:
    print(pais)
    print("-" * 40)