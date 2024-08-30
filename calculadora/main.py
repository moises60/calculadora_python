import tkinter as tk
from tkinter import ttk, messagebox
import math

#ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Científica")

ventana.geometry("400x600")
ventana.resizable(False, False)

#estilo 
style = ttk.Style()
style.configure("TButton", font=("Arial", 18), padding=10)
style.configure("TLabel", font=("Arial", 24))
entrada_texto = tk.StringVar()

#paantalla de la calculadora
pantalla = ttk.Entry(ventana, textvariable=entrada_texto, justify='right', font=("Arial", 24))
pantalla.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=8, padx=10, pady=20)

# Definir la lgica para manejar las operaciones
def insertar_valor(valor):
    actual = entrada_texto.get()
    entrada_texto.set(actual + str(valor))

def calcular():
    try:
        resultado = eval(entrada_texto.get())
        entrada_texto.set(resultado)
    except Exception as e:
        messagebox.showerror("Error", "Error en la operación")
        entrada_texto.set("")

def limpiar():
    entrada_texto.set("")

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
        b = ttk.Button(ventana, text=boton, command=lambda: insertar_valor('math.pi'))
    elif boton == 'log':
        b = ttk.Button(ventana, text=boton, command=lambda: insertar_valor('math.log10('))
    elif boton == 'sin':
        b = ttk.Button(ventana, text=boton, command=lambda: insertar_valor('math.sin('))
    elif boton == 'cos':
        b = ttk.Button(ventana, text=boton, command=lambda: insertar_valor('math.cos('))
    elif boton == 'tan':
        b = ttk.Button(ventana, text=boton, command=lambda: insertar_valor('math.tan('))
    elif boton == 'exp':

        b = ttk.Button(ventana, text=boton, command=lambda: insertar_valor('math.exp('))
    else:
        b = ttk.Button(ventana, text=boton, command=lambda valor=boton: insertar_valor(valor))
    
    b.grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)
    columna += 1
    if columna == 5:
        columna = 0
        fila += 1

#filas y columnas se expandan proporcionalmente
for i in range(5):
    ventana.grid_columnconfigure(i, weight=1)
for i in range(8):

    ventana.grid_rowconfigure(i, weight=1)



ventana.mainloop()
