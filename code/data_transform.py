import pandas as pd
import os

# Definir ruta base
ruta_base = r"D:\dataops_certus"

# Ruta de archivos
archivo_csv = os.path.join(ruta_base, "clientes.csv")
archivo_excel = os.path.join(ruta_base, "clientes_ordenados.xlsx")

try:
    # Leer el archivo CSV
    data = pd.read_csv(archivo_csv, encoding='utf-8')

    # Verificar si la columna "Nombre1" existe
    if "Nombre1" not in data.columns:
        raise ValueError("La columna 'Nombre1' no existe en el archivo CSV.")

    # Ordenar los datos por "Nombre1"
    data_ordenada = data.sort_values(by="Nombre1")

    # Exportar a Excel
    data_ordenada.to_excel(archivo_excel, index=False, encoding='utf-8')

    print(f"Datos ordenados y guardados en {archivo_excel}")
except Exception as e:
    print(f"Error al transformar los datos: {e}")

