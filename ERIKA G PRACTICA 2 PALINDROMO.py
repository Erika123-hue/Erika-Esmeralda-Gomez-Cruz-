
texto = input("OSO")

limpio = texto.replace(" ", "").lower()

if limpio == limpio[::-1]:
    print("¡Sí es un palíndromo!")
else:
    print("No es un palíndromo.")
