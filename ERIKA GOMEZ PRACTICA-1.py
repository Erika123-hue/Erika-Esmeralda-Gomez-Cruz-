import matplotlib .pyplot as plt

y = (1,13,13,11,11,8,8,6,6,3,3,1,1)
x = (1,1,8,8,3,3,7,7,3,3,8,8,1)

plt .plot(x, y)

plt .xlabel('Eje X')
plt .ylabel('Eje y')
plt .title('Grafica de linea simple')
plt .grid(False) # Para mostrar cuadrila

plt .show()
