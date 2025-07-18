import math

x1 = float(input("Ingresa x1: 2"))
y1 = float(input("Ingresa y1:3"))
x2 = float(input("Ingresa x2:6 "))
y2 = float(input("Ingresa y2:7 "))
O = float(input("Ingresa el valor de O:2 "))

Dm = ((x1 + x2) / 2, (y1 + y2) / 2)
print(f"Distancia media Dm: {Dm}")

DE = math.sqrt((x2 - x1)*2 + (y2 - y1)*2)
print(f"Distancia Euclidiana DE: {DE:.2f}")

resultado = DE * O + Dm[0] + Dm[1]
print(f"Resultado aplicando Dm y DE: {resultado:.2f}")
