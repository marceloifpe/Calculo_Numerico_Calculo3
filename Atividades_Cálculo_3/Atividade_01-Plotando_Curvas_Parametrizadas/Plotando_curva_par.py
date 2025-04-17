# Desenvolvido por: Marcelo Augusto de Barros Araújo.
# Disciplina: Cálculo 3.
# Professor: Marcos Maia.
# Instituição: UABJ.
# Curso: Engenharia da Computação.
# Data: 17/04/25.

import matplotlib.pyplot as plt
import numpy as np

# Parâmetros da hélice
altura_total = 10  # 10 cm
num_voltas = 10

# Configura o parâmetro t para 10 voltas completas
t = np.linspace(0, num_voltas * 2 * np.pi, 1000)  # t vai até 10*2π

# Equações paramétricas
x = np.cos(t)            # 1 volta por 2π em t
y = np.sin(t)            # 1 volta por 2π em t
z = (altura_total / (num_voltas * 2 * np.pi)) * t  # Ajusta z para 10 cm

# Plotagem 3D
ax = plt.axes(projection='3d')
ax.plot3D(x, y, z, color='red', linewidth=2)
ax.set_title("Hélice Circular (10 voltas, 10 cm)")
ax.set_zlabel('Z (cm)')
plt.show()