# Ejercicio 1
def ejercicio1():
  """
  Crea un programa que imprima por pantalla el mensaje: "Hola Mundo!".
  """
  print("Hola Mundo!")

# Ejercicio 2
def ejercicio2():
  """
  Crea un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
  Por ejemplo: si el usuario ingresa "Marcos", el programa debe imprimir por pantalla "Hola Marcos!".
  """
  nombre = input("Ingresa tu nombre: ")
  print(f"Hola {nombre}!")

# Ejercicio 3
def ejercicio3():
  """
  Crea un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
  Por ejemplo: si el usuario ingresa "Marcos", "Pérez", "30" y "Argentina", el programa debe imprimir "Soy Marcos Pérez, tengo 30 años y vivo en Argentina".
  """
  nombre = input("Ingresa tu nombre: ")
  apellido = input("Ingresa tu apellido: ")
  edad = input("Ingresa tu edad: ")
  lugar_residencia = input("Ingresa tu lugar de residencia: ")
  print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")

# Ejercicio 4
def ejercicio4():
  """
  Crea un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
  """
  import math
  radio = float(input("Ingresa el radio del círculo: "))
  area = math.pi * radio**2
  perimetro = 2 * math.pi * radio
  print(f"El área del círculo es: {area}")
  print(f"El perímetro del círculo es: {perimetro}")

# Ejercicio 5
def ejercicio5():
  """
  Crea un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
  """
  segundos = int(input("Ingresa la cantidad de segundos: "))
  horas = segundos // 3600
  print(f"{segundos} segundos equivalen a {horas} horas.")

# Ejercicio 6
def ejercicio6():
  """
  Crea un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
  """
  numero = int(input("Ingresa un número: "))
  print(f"Tabla de multiplicar del {numero}:")
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7
def ejercicio7():
  """
  Crea un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
  """
  numero1 = int(input("Ingresa el primer número (distinto de 0): "))
  numero2 = int(input("Ingresa el segundo número (distinto de 0): "))
  print(f"Suma: {numero1 + numero2}")
  print(f"Resta: {numero1 - numero2}")
  print(f"Multiplicación: {numero1 * numero2}")
  print(f"División: {numero1 / numero2}")

# Ejercicio 8
def ejercicio8():
  """
  Crea un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
  Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
  IMC = peso en kg / (altura en m)^2
  """
  altura = float(input("Ingresa tu altura en metros: "))
  peso = float(input("Ingresa tu peso en kilogramos: "))
  imc = peso / altura**2
  print(f"Tu índice de masa corporal es: {imc}")

# Ejercicio 9
def ejercicio9():
  """
  Crea un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
  Tener en cuenta la siguiente equivalencia:
  Temperatura en Fahrenheit = (9/5) * Temperatura en Celsius + 32
  """
  celsius = float(input("Ingresa la temperatura en grados Celsius: "))
  fahrenheit = (9/5) * celsius + 32
  print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")

# Ejercicio 10
def ejercicio10():
  """
  Crea un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
  """
  numero1 = float(input("Ingresa el primer número: "))
  numero2 = float(input("Ingresa el segundo número: "))
  numero3 = float(input("Ingresa el tercer número: "))
  promedio = (numero1 + numero2 + numero3) / 3
  print(f"El promedio de los tres números es: {promedio}")

# Ejecutar los ejercicios
ejercicio1()
ejercicio2()
ejercicio3()
ejercicio4()
ejercicio5()
ejercicio6()
ejercicio7()
ejercicio8()
ejercicio9()
ejercicio10()