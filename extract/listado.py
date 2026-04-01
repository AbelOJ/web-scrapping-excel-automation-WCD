import requests

# Esta es la URL de la API que descubriste en Network.
URL = "https://8ha1x9o9y5-dsn.algolia.net/1/indexes/*/queries"

# Estos son parámetros que la API espera en la URL.
PARAMS = {
    "x-algolia-agent": "Algolia for JavaScript (5.38.0); Search (5.38.0); Browser; instantsearch.js (4.80.0); Vue (2.7.16); Vue InstantSearch (4.21.3); JS Helper (3.26.0)",
    "x-algolia-api-key": "57fd369e98cb7055b68d273f418b74e0",
    "x-algolia-application-id": "8HA1X9O9Y5"
}

# Estos headers hacen que la request se parezca a la del navegador.
HEADERS = {
    "Origin": "https://wecandoo.fr",
    "Referer": "https://wecandoo.fr/",
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Content-Type": "application/json"
}


def obtener_cursos_de_pagina(page):
    """
    Recibe un número de página y devuelve la lista de cursos de esa página.
    Ojo: en la API, la paginación empieza en 0.
    Ejemplo:
    - page = 0  -> primera página
    - page = 1  -> segunda página
    """

    # Este payload es el cuerpo JSON que enviamos a la API.
    # Lo armamos dentro de la función porque lo único que cambia es "page".
    payload = {
        "requests": [
            {
                "indexName": "production_ateliers",
                "attributesToRetrieve": [
                    "id",
                    "atelier_id",
                    "prix",
                    "nom",
                    "short_title",
                    "duration",
                    "city_and_district",
                    "image",
                    "experience_image",
                    "page_url",
                    "new",
                    "_geoloc",
                    "lieu_id",
                    "sous_titre",
                    "craft",
                    "age_min",
                    "age_max",
                    "currency",
                    "group_workshop",
                    "price_incl_vat",
                    "price_excl_vat",
                    "privatization_location_artisan_min",
                    "privatization_location_artisan_max",
                    "privatization_location_customer_min",
                    "privatization_location_customer_max",
                    "privatization_min",
                    "privatization_max",
                    "privatization_location",
                    "artisan_prenom",
                    "pedagogie_prix",
                    "tags",
                    "discounts",
                    "artisan_comment_count",
                    "available_languages",
                    "artisan_id",
                    "artisan_nom",
                    "creations",
                    "format",
                    "nb_pers_max",
                    "nb_pers_min",
                    "note",
                    "offrir_removed",
                    "techniques",
                    "est_privatisable"
                ],
                "distinct": True,
                "facetingAfterDistinct": True,
                "facets": ["craft", "prix", "techniques"],
                "filters": "country:fr",
                "highlightPostTag": "__/ais-highlight__",
                "highlightPreTag": "__ais-highlight__",
                "hitsPerPage": 38,
                "maxValuesPerFacet": 500,
                "page": page,
                "query": ""
            }
        ]
    }

    # Hacemos la request POST a la API.
    response = requests.post(
        URL,
        params=PARAMS,
        headers=HEADERS,
        json=payload,
        timeout=30
    )

    # Si hubo error HTTP (por ejemplo 403, 404, 500), esto lo frena y lo muestra.
    response.raise_for_status()

    # Convertimos la respuesta a JSON de Python (diccionarios y listas).
    data = response.json()

    # La respuesta viene con esta estructura:
    # data["results"][0]["hits"]
    # Ahí está la lista de cursos.
    cursos = data["results"][0]["hits"]

    return cursos


# Esto sirve para probar este archivo por sí solo.
# Si corrés: python extract/listado.py
# se ejecuta este bloque.
if __name__ == "__main__":
    # Le pedimos la página 1 de la API.
    # Eso corresponde a la segunda página visible del sitio.
    cursos = obtener_cursos_de_pagina(1)

    print("Cantidad de cursos encontrados:", len(cursos))

    # Mostramos el primer curso de esa página para comprobar que funcione.
    primer_curso = cursos[0]

    print("\nPrimer curso encontrado:")
    print("Nombre:", primer_curso.get("nom"))
    print("Precio:", primer_curso.get("prix"))
    print("Ciudad:", primer_curso.get("city_and_district"))
    print("URL:", primer_curso.get("page_url"))