from country import CountryAPI

def main()-> None:
    api= CountryAPI()
    nombres=[  # Jhon y Yeleinys
        "japan",
        "hungary",
        "oman",
        "nepal",
        "yemen",            
        "egypt",
        "laos",
        "estonia",
        "india",
        "nigeria",
        "yemen", #-> No encontre otro pais con "Y" xd
        "spain",
    ]
    paises =api.by_nombres_concurrencia(nombres)
    if paises:
        paises[0].comparar(paises[1:])

if __name__ == "__main__":
    main()