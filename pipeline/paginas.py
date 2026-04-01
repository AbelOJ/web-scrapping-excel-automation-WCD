from extract.listado import obtener_cursos_de_pagina


def recorrer_paginas(desde, hasta):
    """
    Recorre varias páginas de la API y junta todos los cursos en una sola lista.

    Parámetros:
    - desde: página inicial de la API
    - hasta: página final de la API

    Ejemplo:
    recorrer_paginas(0, 2)

    Eso recorre:
    - página 0
    - página 1
    - página 2
    """

    todos_los_cursos = []

    # range(desde, hasta + 1) incluye también la última página.
    for page in range(desde, hasta + 1):
        print(f"Leyendo página {page}...")

        # Traemos los cursos de esa página usando la función de extract/listado.py
        cursos_de_esa_pagina = obtener_cursos_de_pagina(page)

        print(f"Se encontraron {len(cursos_de_esa_pagina)} cursos en la página {page}")

        # Sumamos esos cursos a la lista general
        todos_los_cursos.extend(cursos_de_esa_pagina)

    return todos_los_cursos


# Este bloque sirve para probar este archivo solo.
if __name__ == "__main__":
    cursos = recorrer_paginas(0, 1)

    print("\nTotal de cursos juntados:", len(cursos))

    primer_curso = cursos[0]

    print("\nPrimer curso total:")
    print("Nombre:", primer_curso.get("nom"))
    print("Precio:", primer_curso.get("prix"))
    print("Ciudad:", primer_curso.get("city_and_district"))
    print("URL:", primer_curso.get("page_url"))