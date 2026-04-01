from extract.detalle import obtener_detalle_curso
from pipeline.paginas import recorrer_paginas


def recorrer_detalles(cursos):
    """
    Recibe una lista de cursos del listado y,
    para cada uno, entra a su página de detalle.

    Devuelve una nueva lista con los datos del listado
    más los datos del detalle unidos en un solo diccionario.
    """

    cursos_completos = []

    for curso in cursos:
        # Del listado ya tenemos la URL corta del curso.
        url_corta = curso.get("page_url")

        print(f"Leyendo detalle de: {url_corta}")

        # Sacamos el detalle HTML del curso.
        detalle = obtener_detalle_curso(url_corta)

        # Unimos los datos del listado con los del detalle.
        curso_completo = {
            **curso,
            **detalle
        }

        cursos_completos.append(curso_completo)

    return cursos_completos


# Bloque de prueba manual
if __name__ == "__main__":
    # Primero traemos una sola página de cursos.
    cursos_base = recorrer_paginas(0, 0)

    # Para no tardar mucho, probamos solo con los primeros 3 cursos.
    cursos_base = cursos_base[:3]

    cursos_completos = recorrer_detalles(cursos_base)

    print("\nTotal de cursos completos:", len(cursos_completos))

    primer_curso = cursos_completos[0]

    print("\nPrimer curso completo:")
    print("Nombre listado:", primer_curso.get("nom"))
    print("Precio:", primer_curso.get("prix"))
    print("Ciudad:", primer_curso.get("city_and_district"))
    print("URL corta:", primer_curso.get("page_url"))
    print("URL completa:", primer_curso.get("url_completa"))
    print("Título detalle:", primer_curso.get("titulo"))
    print("Descripción detalle:", primer_curso.get("descripcion"))