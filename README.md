# Parcial API Countries

## Integrantes
- Jhon Mindiola — Código: 0182410099
- Yeleinys Gomez — Código: 0182410068

## Descripción
Este proyecto consume la API REST Countries usando Python y la librería requests.
Se modeló la solución con Programación Orientada a Objetos mediante las clases `Country` y `CountryAPI`.

## Países elegidos
- J → Japan
- H → Hungary
- O → Oman
- N → Nepal
- Y → Yemen
- E → Egypt
- L → Laos
- E → Estonia
- I → India
- N → Nigeria
- Y → Yemen (No existen mas paises con "Y")
- S → Spain

## Clase Country
La clase `Country` representa un país y almacena su nombre, capital, población, área y región.
También calcula la densidad poblacional y permite comparar varios países.

## Clase CountryAPI
La clase `CountryAPI` se encarga de hacer las consultas a la API REST Countries.
Incluye métodos para buscar un país por nombre, buscar países por región y consultar varios nombres en paralelo con `ThreadPoolExecutor`.

