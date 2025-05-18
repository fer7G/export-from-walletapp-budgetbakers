from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime, timedelta
import dateparser

# Ruta del archivo HTML
html_path = "registros.html"

# Obtener fecha de modificación del archivo
file_creation_date = datetime.fromtimestamp(os.path.getmtime(html_path)).date()

# Cargar el archivo HTML
with open(html_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Inicializar variables
data = []
current_date = None

# Buscar cada bloque de registros
for record_block in soup.find_all(class_="_3wwqabSSUyshePYhPywONa _1WDK9_g9dlWq0E8o4YpuCW"):
    # Detectar la fecha
    date_div = record_block.find_previous(class_="MhNEgOnlVNRo3U-Ti1ZHP")
    if date_div:
        raw_date = date_div.get_text(strip=True)

        # Normalizar la fecha
        if raw_date.lower() == "hoy": # Substitute for "today" in English
            current_date = file_creation_date
        elif raw_date.lower() == "ayer": # Substitute for "yesterday" in English
            current_date = file_creation_date - timedelta(days=1)
        else:
            # Asegurar que si no hay año, se le pone el del archivo
            parsed_date = dateparser.parse(raw_date, languages=["es"]) # Substitue for "en" in English
            if parsed_date.year == 1900:
                parsed_date = parsed_date.replace(year=file_creation_date.year)
            current_date = parsed_date.date()

    # Extraer la cantidad
    amount_div = record_block.find(class_="zh61r2aVULGpP5-PnSAHX")
    amount = amount_div.get_text(strip=True) if amount_div else "N/A"

    # Extraer la descripción
    description_div = record_block.find(class_="qcICMAjXBzU_8kvhCu6Ir")
    description = description_div.get_text(strip=True) if description_div else "N/A"

    # Extraer la categoría
    category_div = record_block.find(class_="_8i-eheZb5L24RqIZiPgP8")
    category = category_div.get_text(strip=True) if category_div else "N/A"

    # Extraer el pagador/cobrador
    payer_div = record_block.find(class_="_1HvfM2PHFVj--6nRBLVJIb")
    payer = payer_div.get_text(strip=True) if payer_div else "N/A"

    # Extraer etiquetas
    tags_divs = record_block.find_all(class_="_3UT36xJ3h2caZ1l_vTl4-h")
    tags = ", ".join(tag.get_text(strip=True) for tag in tags_divs) if tags_divs else "N/A"

    # Extraer la cuenta asociada
    account_div = record_block.find(class_="_1yNGMXuFq364Pg-thcczh2")
    account = account_div.get_text(strip=True) if account_div else "N/A"

    # Guardar la información en el diccionario
    data.append({
        "Fecha": current_date.isoformat(),
        "Cantidad": amount,
        "Descripción": description,
        "Categoría": category,
        "Pagador/Cobrador": payer,
        "Etiquetas": tags,
        "Cuenta": account
    })

# Crear DataFrame y exportar
df = pd.DataFrame(data)
df.to_csv("transacciones_exportadas.csv", index=False, encoding="utf-8")
print("Archivo CSV generado exitosamente en el mismo directorio del script.")
