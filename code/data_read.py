import pandas as pd
import os

# Definir ruta base
ruta_base = r"D:\dataops_certus"

# Ruta del archivo de entrada y salida
archivo_txt = os.path.join(ruta_base, "Asegurados.txt")
archivo_csv = os.path.join(ruta_base, "clientes.csv")

try:
    # Leer el archivo TXT
    data = pd.read_csv(archivo_txt, delimiter='|', encoding='utf-8')

    # Guardar los datos en un archivo CSV
    data.to_csv(archivo_csv, index=False, encoding='utf-8')

    print(f"Datos leídos y guardados en {archivo_csv}")
except Exception as e:
    print(f"Error al leer el archivo TXT: {e}")

