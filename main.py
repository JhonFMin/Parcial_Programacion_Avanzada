from country import CountryAPI


def main() -> None:
    api = CountryAPI()
    nombres = [
        "spain",
        "denmark",
        "uganda",
        "algeria",
        "romania",
        "oman",
        "japan",
        "austria",
        "nepal"
    ]
    paises = api.by_nombres(nombres)

    if paises:
        paises[0].comparar(paises[1:])


if __name__ == "__main__":
    main()