import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import math

# ---------------------------
# Funciones matemáticas
# ---------------------------
def suma(a, b): return a + b
def resta(a, b): return a - b
def multiplicacion(a, b): return a * b
def division(a, b):
    if b == 0:
        raise ValueError("División entre cero no permitida")
    return a / b
def raiz(a):
    if a < 0:
        raise ValueError("No se puede sacar raíz de número negativo")
    return math.sqrt(a)
def potencia(a, b): return a ** b
def distancia_desde_origen(x, y):
    return math.sqrt(x ** 2 + y ** 2)

# ---------------------------
# Interfaz gráfica
# ---------------------------
ventana = tk.Tk()
ventana.title("Calculadora y Gráfica")
ventana.geometry("650x500")

# Entradas
tk.Label(ventana, text="Valor X:").place(x=30, y=30)
entrada1 = tk.Entry(ventana)
entrada1.place(x=120, y=30)

tk.Label(ventana, text="Valor Y:").place(x=30, y=70)
entrada2 = tk.Entry(ventana)
entrada2.place(x=120, y=70)

# Resultado
resultado_label = tk.Label(ventana, text="Resultado: ", font=("Arial", 14))
resultado_label.place(x=30, y=120)

# Frame para gráfica
ancho_px, alto_px = 400, 300
frame_grafica = tk.Frame(ventana, width=ancho_px, height=alto_px, bg="white")
frame_grafica.place(x=200, y=170)

# Función para mostrar resultado
def mostrar_resultado(texto):
    resultado_label.config(text=f"Resultado: {texto}")

# Función para graficar distancia
def graficar_linea(x, y):
    for widget in frame_grafica.winfo_children():
        widget.destroy()

    dpi = 100
    fig, ax = plt.subplots(figsize=(ancho_px/dpi, alto_px/dpi), dpi=dpi)
    ax.plot([0, x], [0, y], marker='o', color="blue")
    ax.set_title("Distancia desde el origen")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.grid(True)

    # Ajustar ejes para que el punto siempre se vea
    ax.set_xlim(min(0, x) - 1, max(0, x) + 1)
    ax.set_ylim(min(0, y) - 1, max(0, y) + 1)

    canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
    canvas.draw()
    canvas.get_tk_widget().place(x=0, y=0, width=ancho_px, height=alto_px)

# Funciones para cada botón
def operar(funcion, necesita_dos=True, es_distancia=False):
    try:
        if es_distancia:
            x = float(entrada1.get())
            y = float(entrada2.get())
            res = distancia_desde_origen(x, y)
            mostrar_resultado(res)
            graficar_linea(x, y)
        elif necesita_dos:
            a = float(entrada1.get())
            b = float(entrada2.get())
            mostrar_resultado(funcion(a, b))
        else:
            a = float(entrada1.get())
            mostrar_resultado(funcion(a))
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Botones de operaciones
tk.Button(ventana, text="+", width=5, command=lambda: operar(suma)).place(x=30, y=170)
tk.Button(ventana, text="-", width=5, command=lambda: operar(resta)).place(x=90, y=170)
tk.Button(ventana, text="*", width=5, command=lambda: operar(multiplicacion)).place(x=150, y=170)
tk.Button(ventana, text="/", width=5, command=lambda: operar(division)).place(x=210, y=170)
tk.Button(ventana, text="Raíz", width=5, command=lambda: operar(raiz, necesita_dos=False)).place(x=30, y=210)
tk.Button(ventana, text="Potencia", width=8, command=lambda: operar(potencia)).place(x=90, y=210)
tk.Button(ventana, text="Distancia", width=8, command=lambda: operar(None, es_distancia=True)).place(x=180, y=210)

ventana.mainloop()
