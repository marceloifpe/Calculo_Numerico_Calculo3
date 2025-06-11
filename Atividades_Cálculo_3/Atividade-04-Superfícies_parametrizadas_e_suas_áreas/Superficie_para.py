import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parâmetros do cilindro
r = 2  # raio (pois x² + y² = 4 → r = 2)
h = 3  # altura

# Criação da malha (grade de pontos)
theta = np.linspace(0, 2 * np.pi, 100)
z = np.linspace(0, h, 30)
Theta, Z = np.meshgrid(theta, z)

X = r * np.cos(Theta)
Y = r * np.sin(Theta)

# Plotagem
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Superfície do cilindro
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='black', alpha=0.8)

# Título e rótulos
ax.set_title('Visualização do Cilindro x²+y² = 4 com Altura 3')
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

# Ajustes dos limites
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([0, 3.5])

plt.tight_layout()
plt.show()
