import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, nombre, apellido, salario, dias_trabajados):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.dias_trabajados = dias_trabajados

class CalculadoraNomina:
    def calcular_prima(self, salario, dias):
        return (salario * dias) / 360
    
    def cesantias_causadas(self, salario, dias):
        return (salario * dias) / 360
    
    def intereses_cesantias(self, cesantias_causadas, dias):
        return (cesantias_causadas * dias * 0.12) / 360
    
    def vacaciones(self, salario, dias):
        return (salario * dias) / 720
    
    def calcular_salario_con_aumento(self, salario, porcentaje):
        return salario * (1 + porcentaje/100)
    

class InterfazNomina:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Calculadora de Nómina")
        ventana.geometry("400x600")

        # Nombre
        tk.Label(ventana, text="Nombre:").pack(pady=5)
        self.nombre_entry = tk.Entry(ventana)
        self.nombre_entry.pack(pady=5)

        # Apellido
        tk.Label(ventana, text="Apellido:").pack(pady=5)
        self.apellido_entry = tk.Entry(ventana)
        self.apellido_entry.pack(pady=5)

        # Días trabajados
        tk.Label(ventana, text="Días laborados:").pack(pady=5)
        self.dias_entry = tk.Entry(ventana)
        self.dias_entry.pack(pady=5)

        # Salario
        tk.Label(ventana, text="Salario:").pack(pady=5)
        self.salario_entry = tk.Entry(ventana)
        self.salario_entry.pack(pady=5)

        # Aumento
        tk.Label(ventana, text="Aumento (%):").pack(pady=5)
        self.aumento_entry = tk.Entry(ventana)
        self.aumento_entry.pack(pady=5)

        # Botón Calcular
        self.calcular_btn = tk.Button(ventana, text="Calcular", command=self.calcular)
        self.calcular_btn.pack(pady=10)

        # Botón Salir
        self.salir_btn = tk.Button(ventana, text="Salir", command=ventana.quit)
        self.salir_btn.pack(pady=10)

        # Botón para exportar txt
        self.exportar_btn = tk.Button(ventana, text="Exportar txt", command=self.exportar_txt)
        self.exportar_btn.pack(pady=10)

        # Área de resultados
        self.resultados_text = tk.Text(ventana, height=10, width=50)
        self.resultados_text.pack(pady=10)
        
    def calcular(self):
            empleado = Empleado(
                self.nombre_entry.get(), 
                self.apellido_entry.get(),
                float(self.salario_entry.get()),
                int(self.dias_entry.get())
            )

            # Crear calculadora
            calculadora = CalculadoraNomina()

            # Calcular conceptos
            prima = calculadora.calcular_prima(empleado.salario, empleado.dias_trabajados)
            salario_con_aumento = calculadora.calcular_salario_con_aumento(
                empleado.salario, 
                float(self.aumento_entry.get()))

            cesantias_causadas = calculadora.cesantias_causadas(empleado.salario, empleado.dias_trabajados)
            intereses_cesantias = calculadora.intereses_cesantias(cesantias_causadas, empleado.dias_trabajados)
            vacaciones = calculadora.vacaciones(empleado.salario, empleado.dias_trabajados)

            subsidio_transporte = 140.606
            
            # Limpiar resultados anteriores
            self.resultados_text.delete(1.0, tk.END)

            # Mostrar resultados
            self.resultados_text.insert(tk.END, f"Nombre: {empleado.nombre} {empleado.apellido}\n")
            self.resultados_text.insert(tk.END, f"Días Laborados: {empleado.dias_trabajados}\n")
            self.resultados_text.insert(tk.END, f"Prima: ${int(prima)}\n")
            self.resultados_text.insert(tk.END, f"Cesantías Causadas: ${int(cesantias_causadas)}\n")
            self.resultados_text.insert(tk.END, f"Intereses Cesantías: ${int(intereses_cesantias)}\n")
            self.resultados_text.insert(tk.END, f"Vacaciones: ${int(vacaciones)}\n")
            self.resultados_text.insert(tk.END, f"Salario con Aumento: ${int(salario_con_aumento)}\n")
            self.resultados_text.insert(tk.END, f"Subsidio de Transporte: ${subsidio_transporte}\n")
            self.resultados_text.insert(tk.END, f"Salario Total: ${int(salario_con_aumento + subsidio_transporte)}\n")

    def exportar_txt(self):
        with open("nomina.txt", "w") as archivo:
            archivo.write(self.resultados_text.get(1.0, tk.END))
        messagebox.showinfo("Éxito", "Resultados exportados a nomina.txt")

def main():
    root = tk.Tk()
    app = InterfazNomina(root)
    root.mainloop()

if __name__ == "__main__":
    main()