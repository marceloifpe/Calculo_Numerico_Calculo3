import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)

x, y = np.meshgrid(x, y)

# Campo Vetorial
P = y
Q = np.sin(x)

# Gráfico com melhorias visuais
plt.figure(figsize=(10, 6))                 # Aumenta o tamanho da figura
plt.quiver(x, y, P, Q, color='Red', scale=300)  # Cor personalizada e escala ajustada
plt.title('Campo Vetorial: P = y, Q = sin(x)', fontsize=12)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.axis('equal')  # Mantém proporções dos eixos iguais
plt.show()