import numpy as np
import matplotlib.pyplot as plt

def plot_distances(center=(0, 0), max_distance=10, step=1):
    fig, axes = plt.subplots(1, 2, figsize=(10, 6))
    fig.suptitle('Distancia Euclidiana vs Distancia Manhattan')
    
    # Distancia Euclidiana (círculos)
    axes[0].set_title('Distancia Euclidiana')
    axes[0].set_aspect('equal')
    for d in range(step, max_distance + step, step):
        circle = plt.Circle(center, d, edgecolor='b', facecolor='none', linestyle='--')
        axes[0].add_patch(circle)
        axes[0].text(0, d + 0.3, f'{d}', fontsize=7, ha='center', color='black')  # Etiqueta con la distancia
    axes[0].plot(*center, 'ro', label='Centro')  # Punto central
    axes[0].set_xlim(-max_distance-1, max_distance+1)
    axes[0].set_ylim(-max_distance-1, max_distance+1)
    axes[0].grid(True)
    axes[0].text(0, -max_distance-4, '$d = \sqrt{(x-x_0)^2 + (y-y_0)^2}$', fontsize=10, ha='center')

    # Distancia Manhattan (rombos)
    axes[1].set_title('Distancia Manhattan')
    axes[1].set_aspect('equal')
    for d in range(step, max_distance + step, step):
        diamond = plt.Polygon([
            (center[0], center[1] + d),
            (center[0] + d, center[1]),
            (center[0], center[1] - d),
            (center[0] - d, center[1])
        ], edgecolor='g', facecolor='none', linestyle='--')
        axes[1].add_patch(diamond)
        axes[1].text(0, d + 0.3, f'{d}', fontsize=7, ha='center', color='black')  # Etiqueta con la distancia
    axes[1].plot(*center, 'ro', label='Centro')  # Punto central
    axes[1].set_xlim(-max_distance-1, max_distance+1)
    axes[1].set_ylim(-max_distance-1, max_distance+1)
    axes[1].grid(True)
    axes[1].text(0, -max_distance-4, '$d = |x-x_0| + |y-y_0|$', fontsize=10, ha='center')

    plt.tight_layout()
    plt.show()

plot_distances()
