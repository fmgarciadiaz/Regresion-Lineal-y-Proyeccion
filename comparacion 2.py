import matplotlib.pyplot as plt
import numpy as np

# Definir el punto P
punto_p = np.array([2, 3])

# Definir la recta (usando dos puntos para definirla)
punto_recta1 = np.array([-1, 1])
punto_recta2 = np.array([5, 4])

# Calcular la pendiente y la intersección de la recta
pendiente = (punto_recta2[1] - punto_recta1[1]) / (punto_recta2[0] - punto_recta1[0])
interseccion = punto_recta1[1] - pendiente * punto_recta1[0]

# Función para la recta
def recta(x):
    return pendiente * x + interseccion

# Rango para dibujar la recta
x_recta = np.linspace(-2, 7, 400)
y_recta = recta(x_recta)

# --- Calcular y graficar la Distancia Euclidiana ---
# Proyectar el punto P sobre la recta para encontrar el punto más cercano en euclidiana
a_recta = pendiente
b_recta = -1
c_recta = interseccion

x0, y0 = punto_p

x_euclidiano = x0 - a_recta * (a_recta * x0 + b_recta * y0 + c_recta) / (a_recta**2 + b_recta**2)
y_euclidiano = y0 - b_recta * (a_recta * x0 + b_recta * y0 + c_recta) / (a_recta**2 + b_recta**2)
punto_recta_euclidiano = np.array([x_euclidiano, y_euclidiano])

# Distancia Euclidiana
distancia_euclidiana = np.linalg.norm(punto_p - punto_recta_euclidiano)

# --- Calcular y graficar una Distancia Manhattan aproximada ---
punto_recta_manhattan_x = punto_p[0]
punto_recta_manhattan_y = recta(punto_recta_manhattan_x)
punto_recta_manhattan = np.array([punto_recta_manhattan_x, punto_recta_manhattan_y])

# Distancia Manhattan
distancia_manhattan = np.sum(np.abs(punto_p - punto_recta_manhattan))


# --- Graficar ---
plt.figure(figsize=(10, 10))
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.7)

# Graficar la recta
plt.plot(x_recta, y_recta, color='black', label=None) # **Recta en negro y label=None para eliminar de leyenda**

# Graficar el punto P
plt.plot(punto_p[0], punto_p[1], 'ro', markersize=8, label='Punto P')
plt.annotate('P', punto_p, textcoords="offset points", xytext=(0,10), ha='center')

# --- Graficar Distancia Euclidiana ---
plt.plot(punto_recta_euclidiano[0], punto_recta_euclidiano[1], 'bo', markersize=8, label='Punto Recta Euclidiano')
plt.plot([punto_p[0], punto_recta_euclidiano[0]], [punto_p[1], punto_recta_euclidiano[1]], color='blue', linestyle='dashed', label=f'Dist. Euclidiana = {distancia_euclidiana:.2f}')
plt.annotate('Pe', punto_recta_euclidiano, textcoords="offset points", xytext=(0,-15), ha='center', color='blue')

# Circulo Euclidiano
circulo_euclidiano = plt.Circle(punto_p, distancia_euclidiana, color='blue', fill=False, linestyle='--', linewidth=1.5, label=None) # label=None para eliminar de la leyenda
plt.gca().add_patch(circulo_euclidiano)


# --- Graficar Distancia Manhattan ---
plt.plot(punto_recta_manhattan[0], punto_recta_manhattan[1], 'ro', color='green', markersize=8, label='Punto Recta Manhattan (Aprox)')
plt.plot([punto_p[0], punto_recta_manhattan[0]], [punto_p[1], punto_recta_manhattan[1]], color='green', linestyle='dashed', label=f'Dist. Manhattan = {distancia_manhattan:.2f}')
plt.annotate('Pm', punto_recta_manhattan, textcoords="offset points", xytext=(0,-15), ha='center', color='green')

# Rombo Manhattan
from matplotlib.patches import Polygon

def generar_rombo_manhattan(centro, distancia):
    x0, y0 = centro
    d = distancia
    vertices_rombo = [
        [x0, y0 + d],
        [x0 + d, y0],
        [x0, y0 - d],
        [x0 - d, y0]
    ]
    return Polygon(vertices_rombo, closed=True, edgecolor='green', facecolor='none', linestyle='--', linewidth=1.5, label=None) # label=None para eliminar de la leyenda

rombo_manhattan = generar_rombo_manhattan(punto_p, distancia_manhattan)
plt.gca().add_patch(rombo_manhattan)


# Configuración del gráfico - LIMITES AJUSTADOS PARA ZOOM
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Distancia de punto a una recta (euclidiana vs manhattan)') # Título actualizado
plt.xlim([1, 3]) # LIMITES X MODIFICADOS
plt.ylim([2, 4]) # LIMITES Y MODIFICADOS
plt.gca().set_aspect('equal', adjustable='box') # Aspecto igual para que circulo se vea como circulo
plt.legend(loc='upper right', fontsize='small')

plt.show()