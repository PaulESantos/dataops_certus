import matplotlib.pyplot as plt
import numpy as np
import os

# Crear la carpeta [graficos] si no existe
if not os.path.exists('graficos'):
    os.makedirs('graficos')

# Generar datos aleatorios
np.random.seed(42)  # Fijar una semilla para reproducibilidad
x = np.linspace(0, 10, 100)  # 100 puntos equiespaciados entre 0 y 10
y = np.random.rand(100)  # 100 valores aleatorios entre 0 y 1

# Crear el gráfico
plt.figure(figsize=(8, 5))  # Tamaño del gráfico
plt.plot(x, y, label='Datos Aleatorios', color='blue', linestyle='-', marker='o', markersize=4)

# Personalizar el gráfico
plt.title('Gráfico Inicializado con Datos Aleatorios')  # Título
plt.xlabel('Eje X')  # Etiqueta del eje X
plt.ylabel('Eje Y')  # Etiqueta del eje Y
plt.grid(True)  # Mostrar cuadrícula
plt.legend()  # Mostrar leyenda

# Guardar el gráfico en la carpeta [graficos]
plt.savefig('D:/dataops_certus/graficos/grafico_aleatorio.png', dpi=300, bbox_inches='tight')

# Mostrar el gráfico
plt.show()
