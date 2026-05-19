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
        "Yibuti", #-> No encontre otro pais con "Y" xd, este no sale en la API, por ende, dara un error.
        "spain",
    ]
    paises =api.by_nombres(nombres)
    if paises:
        paises[0].comparar(paises[1:])

if __name__ == "__main__":
    main()