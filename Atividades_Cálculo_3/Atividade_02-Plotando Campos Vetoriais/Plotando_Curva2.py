import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 6)
y = np.linspace(-10, 10, 6)
z = np.linspace(1, 10, 5)

x, y, z = np.meshgrid(x, y, z)

# Campo Vetorial
P = y / z
Q = -x / z
R = z / 4

# Gráfico 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Campo vetorial com melhorias visuais
ax.quiver(x, y, z, P, Q, R, color='Red', length=1.5, normalize=False, linewidth=0.5)

# Títulos e rótulos
ax.set_title('Campo Vetorial 3D: P = y/z, Q = -x/z, R = z/4', fontsize=12)
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

plt.tight_layout()
plt.show()