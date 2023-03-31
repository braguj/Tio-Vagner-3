import matplotlib.pyplot as plt

# Criar uma figura e um eixo
fig, ax = plt.subplots()

# Adicionar três círculos
c1 = plt.Circle((0.5, 0.7), 0.1, color='blue', fill=False)
c2 = plt.Circle((0.4, 0.6), 0.1, color='red', fill=False)
c3 = plt.Circle((0.550, 0.570), 0.1, color='green', fill=False)
ax.add_artist(c1)
ax.add_artist(c2)
ax.add_artist(c3)

# Adicionar uma grade para ajudar na visualização
ax.grid()

# Mostrar o resultado
plt.show()
