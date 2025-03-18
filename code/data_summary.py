import os
import pandas as pd

# Definir ruta base
ruta_base = r"D:\dataops_certus"

# Ruta de archivos
archivo_excel = os.path.join(ruta_base, "clientes_ordenados.xlsx")

# Cargar el dataset final
df = pd.read_excel(archivo_excel)  # Cambiado de read_csv a read_excel

# Generar un resumen
summary = f"""
Dataset Summary:
----------------
- Numero de filas: {df.shape[0]}
- Numero de columnas: {df.shape[1]}
- Columnas: {', '.join(df.columns)}
"""

# Definir la ruta del archivo de resumen
ruta_summary = os.path.join(ruta_base, "summary.txt")

# Crear la carpeta de logs si no existe
os.makedirs(os.path.dirname(ruta_summary), exist_ok=True)

# Guardar el resumen en un archivo
with open(ruta_summary, "w") as f:
    f.write(summary)

print("Resumen generado exitosamente.")
