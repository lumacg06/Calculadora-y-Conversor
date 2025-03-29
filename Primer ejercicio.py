import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

# Configurar ventana principal
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Convertidor de Temperaturas')

def salir():
    ventana.quit()
    ventana.destroy()
    sys.exit()

def crear_menu():
    menu_principal = Menu(ventana)
    submenu_archivo = Menu(menu_principal, tearoff=0)
    submenu_archivo.add_command(label='Guardar', command=guardar_resultado)
    submenu_archivo.add_command(label='Salir', command=salir)
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
    ventana.config(menu=menu_principal)

def convertir_celsius_fahrenheit():
        celsius = float(entrada1.get())
        fahrenheit = (celsius * 9/5) + 32
        resultado.config(text=f"{celsius}°C = {fahrenheit, 1}°F")


def convertir_fahrenheit_celsius():
        fahrenheit = float(entrada1.get())
        celsius = (fahrenheit - 32) * 5/9
        resultado.config(text=f"{fahrenheit}°F = {celsius, 1}°C")

def guardar_resultado():
        texto_resultado = resultado.cget("text")
        with open("conversiones.txt", "a") as archivo:
            archivo.write(texto_resultado + "\n")
        messagebox.showinfo("Éxito", "Resultado guardado en conversiones.txt")

# Etiqueta de instrucción
etiqueta_instruccion = ttk.Label(ventana, text="Ingrese la temperatura:")
etiqueta_instruccion.grid(row=0, column=0, padx=10, pady=10)

# Campo de entrada
entrada1 = ttk.Entry(ventana, width=30, justify=tk.RIGHT)
entrada1.grid(row=0, column=1, padx=10, pady=10)

# Botón Celsius a Fahrenheit
boton_celsius_fahrenheit = ttk.Button(
    ventana, 
    text="Celsius a Fahrenheit", 
    command=convertir_celsius_fahrenheit
)
boton_celsius_fahrenheit.grid(row=1, column=0, padx=10, pady=10)

# Botón Fahrenheit a Celsius
boton_fahrenheit_celsius = ttk.Button(
    ventana, 
    text="Fahrenheit a Celsius", 
    command=convertir_fahrenheit_celsius
)
boton_fahrenheit_celsius.grid(row=1, column=1, padx=10, pady=10)

# Etiqueta de resultado
resultado = ttk.Label(ventana, text="Resultado", font=("Arial", 12))
resultado.grid(row=2, column=1, padx=10, pady=10)


crear_menu()
ventana.mainloop()