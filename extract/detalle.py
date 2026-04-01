import requests
from bs4 import BeautifulSoup


def obtener_detalle_curso(url_corta):
    """
    Recibe una URL corta del curso, por ejemplo:
    /atelier/burrata-stracciatella-julien-fromage-paris

    Entra a la página del curso y devuelve algunos datos de detalle.
    """

    # La URL que viene del listado es relativa, por eso la completamos.
    url_completa = "https://wecandoo.fr" + url_corta

    # Headers básicos para que la request se parezca más a un navegador real.
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "es-AR,es;q=0.9,en;q=0.8"
    }

    # Pedimos el HTML de la página del curso.
    response = requests.get(url_completa, headers=headers, timeout=30)
    response.raise_for_status()

    # Parseamos el HTML.
    soup = BeautifulSoup(response.text, "html.parser")

    # Diccionario final con los datos que queremos sacar.
    detalle = {
        "url_completa": url_completa,
        "titulo": None,
        "descripcion": None
    }

    # ------------------------------------------------------------
    # 1) Intentamos sacar el título desde meta property="og:title"
    # ------------------------------------------------------------
    meta_og_title = soup.find("meta", attrs={"property": "og:title"})
    if meta_og_title and meta_og_title.get("content"):
        detalle["titulo"] = meta_og_title.get("content").strip()

    # Si no apareció, probamos con <title>
    if detalle["titulo"] is None and soup.title:
        detalle["titulo"] = soup.title.get_text(strip=True)

    # ------------------------------------------------------------
    # 2) Intentamos sacar la descripción desde og:description
    # ------------------------------------------------------------
    meta_og_description = soup.find("meta", attrs={"property": "og:description"})
    if meta_og_description and meta_og_description.get("content"):
        detalle["descripcion"] = meta_og_description.get("content").strip()

    # Si no apareció, probamos con meta name="description"
    if detalle["descripcion"] is None:
        meta_description = soup.find("meta", attrs={"name": "description"})
        if meta_description and meta_description.get("content"):
            detalle["descripcion"] = meta_description.get("content").strip()

    return detalle


# Bloque de prueba manual
if __name__ == "__main__":
    url_prueba = "/atelier/burrata-stracciatella-julien-fromage-paris"

    detalle = obtener_detalle_curso(url_prueba)

    print("URL completa:", detalle["url_completa"])
    print("Título:", detalle["titulo"])
    print("Descripción:", detalle["descripcion"])