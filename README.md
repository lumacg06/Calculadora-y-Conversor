# Calculadora y Conversor

Este proyecto contiene dos aplicaciones desarrolladas en Python con interfaces gráficas utilizando `tkinter`. Cada aplicación tiene un propósito específico: una calculadora de nómina y un convertidor de temperaturas.

## Archivos

1. **Primer ejercicio.py**: Convertidor de Temperaturas
2. **Segundo ejercicio.py**: Calculadora de Nómina

## Primer ejercicio.py: Convertidor de Temperaturas

### Descripción
Esta aplicación permite convertir temperaturas entre Celsius y Fahrenheit. Incluye una interfaz gráfica para ingresar la temperatura, realizar la conversión y guardar los resultados en un archivo de texto.

### Funcionalidades
- Convertir de Celsius a Fahrenheit.
- Convertir de Fahrenheit a Celsius.
- Guardar los resultados en un archivo llamado `conversiones.txt`.

### Uso
1. Ingrese la temperatura en el campo de texto.
2. Presione el botón correspondiente para realizar la conversión.
3. El resultado se mostrará en la interfaz y puede guardarse en un archivo.


## Segundo ejercicio.py: Calculadora de Nómina

### Descripción
Esta aplicación calcula conceptos relacionados con la nómina de un empleado, como prima, cesantías, intereses de cesantías, vacaciones y salario con aumento. Los resultados pueden exportarse a un archivo de texto.

### Funcionalidades
- Calcular prima, cesantías, intereses de cesantías y vacaciones.
- Calcular el salario con un aumento porcentual.
- Exportar los resultados a un archivo llamado `nomina.txt`.

### Uso
1. Ingrese los datos del empleado (nombre, apellido, salario, días trabajados y porcentaje de aumento).
2. Presione el botón "Calcular" para obtener los resultados.
3. Los resultados se mostrarán en la interfaz y pueden exportarse a un archivo.

## Requisitos
- Python 3.x
- Biblioteca `tkinter` (incluida en Python por defecto)

## Ejecución
Ejecute cualquiera de los archivos `.py` para iniciar la aplicación correspondiente:
```bash
python "Primer ejercicio.py"
python "Segundo ejercicio.py"
