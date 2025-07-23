import matplotlib.pyplot as plt

# Valores fijos
color = 'pink'    # Color de la letra
tamaño = 250        # Tamaño de la letra
peso = 'bold'       # Grosor (normal o bold)

# Dibujar la letra E
plt.text(0.5, 0.5, 'E', fontsize=tamaño, color=color, fontweight=peso, ha='center', va='center')
plt.axis('off')
plt.show()
