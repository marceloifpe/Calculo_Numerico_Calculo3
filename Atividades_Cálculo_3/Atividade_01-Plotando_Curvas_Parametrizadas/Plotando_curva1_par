# Desenvolvido por: Marcelo Augusto de Barros Araújo.
# Disciplina: Cálculo 3.
# Professor: Marcos Maia.
# Instituição: UABJ.
# Curso: Engenharia da Computação.
# Data: 17/04/25.

import numpy as np
import matplotlib.pyplot as plt

# Parâmetro t
t = np.linspace(0, 2 * np.pi, 1000)

# Equações paramétricas
x = np.sin(t) + 0.5 * np.cos(5 * t) + 0.25 * np.sin(13 * t)
y = np.cos(t) + 0.5 * np.sin(5 * t) + 0.25 * np.cos(13 * t)

# Plotagem da curva 1
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='red')
plt.title('Curva Parametrizada 1')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.grid(True)
plt.show()