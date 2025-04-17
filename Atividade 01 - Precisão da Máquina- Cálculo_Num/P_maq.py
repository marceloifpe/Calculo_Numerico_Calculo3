# Desenvolvido por: Marcelo Augusto de Barros Araújo.
# Disciplina: Cálculo Numérico.
# Professor: Marcos Maia.
# Instituição: UABJ.
# Curso: Engenharia da Computação.
# Data: 17/04/25.

A = 1
S = 2
cont = 0

while S > 1:
    A = A / 2
    S = A + 1
    cont += 1

print('Precisão da máquina:', 2 * A) # Precisão da máquina foi dividido até atingir o limite de distinção
print('Iterações realizadas:', cont) # Número de iterações necessárias até ser igual a 1
# Justificativa: A repetição só para quando s for igual a 1, ou seja, quando A é tão pequeno que, ao somá-lo a 1,
# a máquina não consegue mais representar a diferença. Esse valor não é zero,
# mas sim o menor número positivo representável no sistema, conhecido como ε (epsilon da máquina).
# Um float (32 bits) usa 24 bits para a mantissa, o que equivale a cerca de 7 dígitos decimais de precisão.
# Um double (64 bits) usa 53 bits na mantissa, permitindo cerca de 15 dígitos decimais.
# Portanto, o double é muito mais preciso, pois tem precisão dupla e consegue representar números menores (ε menor),
# e ocupa o dobro do espaço na memória em relação ao float.