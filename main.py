import tkinter as tk
from tkinter import ttk, messagebox
import math

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Científica")

ventana.geometry("500x700")
ventana.resizable(False, False)

# Estilo
style = ttk.Style()
style.configure("TButton", font=("Arial", 24), padding=10)
style.configure("TEntry", font=("Arial", 34))
entrada_texto = tk.StringVar()

#paantalla de la calculadora
pantalla = ttk.Entry(ventana, textvariable=entrada_texto, justify='right', font=("Arial", 24))
pantalla.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=8, padx=10, pady=20)

# Definir la lógica para manejar las operaciones
def insertar_valor(valor):
    actual = entrada_texto.get()
    entrada_texto.set(actual + str(valor))

def calcular():
    try:
        # Limitar las funciones disponibles en eval
        entorno_seguro = {'__builtins__': None}
        entorno_seguro.update(math.__dict__)
        resultado = eval(entrada_texto.get(), entorno_seguro)
        entrada_texto.set(resultado)
    except Exception as e:
        messagebox.showerror("Error", "Error en la operación")
        entrada_texto.set("")

def limpiar():
    entrada_texto.set("")

def tecla_presionada(event):
    tecla = event.char
    if tecla in '0123456789.+-*/()':
        insertar_valor(tecla)
    elif tecla == '\r':  # Enter
        calcular()
    elif tecla == '\x08':  # Backspace
        limpiar()

ventana.bind('<Key>', tecla_presionada)

botones = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', 'x²',
    '1', '2', '3', '-', '√',
    '0', '.', '=', '+', 'π',
    'log', 'sin', 'cos', 'tan', 'exp',
    '(', ')'
]

fila = 1
columna = 0
for boton in botones:
    if boton == '=':
        b = ttk.Button(ventana, text=boton, command=calcular)
    elif boton == 'C':
        b = ttk.Button(ventana, text=boton, command=limpiar)
    elif boton == 'x²':
        b = ttk.Button(ventana, text=boton, command=lambda: insertar_valor('**2'))
    elif boton == '√':
        b = ttk.Button(ventana, text=boton, command=lambda: insertar_valor('**(1/2)'))
    elif boton == 'π':
        b = ttk.Button(ventana, text=boton, command=lambda: insertar_valor('pi'))
    elif boton == 'log':
        b = ttk.Button(ventana, text=boton, command=lambda: insertar_valor('log('))
    elif boton == 'sin':
        b = ttk.Button(ventana, text=boton, command=lambda: insertar_valor('sin('))
    elif boton == 'cos':
        b = ttk.Button(ventana, text=boton, command=lambda: insertar_valor('cos('))
    elif boton == 'tan':
        b = ttk.Button(ventana, text=boton, command=lambda: insertar_valor('tan('))
    elif boton == 'exp':
        b = ttk.Button(ventana, text=boton, command=lambda: insertar_valor('exp('))
    else:
        b = ttk.Button(ventana, text=boton, command=lambda valor=boton: insertar_valor(valor))
    
    b.grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)
    columna += 1
    if columna == 5:
        columna = 0
        fila += 1

# Hacer que las filas y columnas se expandan proporcionalmente
for i in range(5):
    ventana.grid_columnconfigure(i, weight=1)
for i in range(fila + 1):
    ventana.grid_rowconfigure(i, weight=1)

ventana.mainloop()
