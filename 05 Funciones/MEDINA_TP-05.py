import math

# --- Definición de Funciones ---

# Ejercicio 1
def imprimir_hola_mundo():
    """Imprime el mensaje 'Hola Mundo!' en la pantalla."""
    print("Hola Mundo!")

# Ejercicio 2
def saludar_usuario(nombre):
    """
    Recibe un nombre y devuelve un saludo personalizado.
    Ej: saludar_usuario("Marcos") -> "Hola Marcos!"
    """
    return f"Hola {nombre}!"

# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    """Recibe datos personales e imprime un mensaje formateado."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4
def calcular_area_circulo(radio):
    """Calcula y devuelve el área de un círculo dado su radio."""
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    """Calcula y devuelve el perímetro de un círculo dado su radio."""
    return 2 * math.pi * radio

# Ejercicio 5
def segundos_a_horas(segundos):
    """Convierte una cantidad de segundos a horas."""
    return segundos / 3600

# Ejercicio 6
def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar de un número del 1 al 10."""
    print(f"--- Tabla del {numero} ---")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7
def operaciones_basicas(a, b):
    """Realiza suma, resta, multiplicación y división de dos números."""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # Manejo de la división por cero
    if b != 0:
        division = a / b
    else:
        division = "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)

# Ejercicio 8
def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).
    Peso en kg, altura en metros.
    """
    if altura > 0:
        return peso / (altura ** 2)
    else:
        return "Altura no puede ser cero."

# Ejercicio 9
def celsius_a_fahrenheit(celsius):
    """Convierte una temperatura de grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

# Ejercicio 10
def calcular_promedio(a, b, c):
    """Calcula y devuelve el promedio de tres números."""
    return (a + b + c) / 3

# --- Programa Principal ---

if __name__ == "__main__":
    print("### EJERCICIO 1 ###")
    imprimir_hola_mundo()
    print("-" * 30)

    print("### EJERCICIO 2 ###")
    nombre_usuario = input("Por favor, ingresa tu nombre: ")
    saludo = saludar_usuario(nombre_usuario)
    print(saludo)
    print("-" * 30)

    print("### EJERCICIO 3 ###")
    nombre_personal = input("Ingresa tu nombre: ")
    apellido_personal = input("Ingresa tu apellido: ")
    edad_personal = input("Ingresa tu edad: ")
    residencia_personal = input("Ingresa tu lugar de residencia: ")
    informacion_personal(nombre_personal, apellido_personal, edad_personal, residencia_personal)
    print("-" * 30)

    print("### EJERCICIO 4 ###")
    radio_circulo = float(input("Ingresa el radio del círculo: "))
    area = calcular_area_circulo(radio_circulo)
    perimetro = calcular_perimetro_circulo(radio_circulo)
    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")
    print("-" * 30)

    print("### EJERCICIO 5 ###")
    segundos_ingresados = int(input("Ingresa una cantidad de segundos: "))
    horas = segundos_a_horas(segundos_ingresados)
    print(f"{segundos_ingresados} segundos equivalen a {horas:.4f} horas.")
    print("-" * 30)

    print("### EJERCICIO 6 ###")
    numero_tabla = int(input("Ingresa un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero_tabla)
    print("-" * 30)

    print("### EJERCICIO 7 ###")
    num1_ops = float(input("Ingresa el primer número para las operaciones: "))
    num2_ops = float(input("Ingresa el segundo número para las operaciones: "))
    suma, resta, mult, div = operaciones_basicas(num1_ops, num2_ops)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {mult}")
    print(f"División: {div}")
    print("-" * 30)

    print("### EJERCICIO 8 ###")
    peso_kg = float(input("Ingresa tu peso en kg: "))
    altura_m = float(input("Ingresa tu altura en metros: "))
    imc = calcular_imc(peso_kg, altura_m)
    if isinstance(imc, str):
        print(imc)
    else:
        print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")
    print("-" * 30)

    print("### EJERCICIO 9 ###")
    temp_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
    print(f"{temp_celsius}°C equivale a {temp_fahrenheit}°F.")
    print("-" * 30)

    print("### EJERCICIO 10 ###")
    num1_prom = float(input("Ingresa el primer número para el promedio: "))
    num2_prom = float(input("Ingresa el segundo número para el promedio: "))
    num3_prom = float(input("Ingresa el tercer número para el promedio: "))
    promedio = calcular_promedio(num1_prom, num2_prom, num3_prom)
    print(f"El promedio de los tres números es: {promedio}")
    print("-" * 30)