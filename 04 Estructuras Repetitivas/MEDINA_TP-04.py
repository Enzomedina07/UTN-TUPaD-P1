import random

# Actividad 1
print("Actividad 1: Números del 0 al 100")
for i in range(101):
    print(i)

# Actividad 2
print("\nActividad 2: Cantidad de dígitos de un número")
numero = int(input("Ingrese un número entero: "))
print(f"El número tiene {len(str(abs(numero)))} dígitos.")



inicio = int(input("Ingrese el número inicial: "))
fin = int(input("Ingrese el número final: "))
suma = sum(range(inicio, fin + 1))
print(f"La suma de los números entre {inicio} y {fin} es: {suma}")

# Actividad 4
print("\nActividad 4: Suma de números hasta ingresar 0")
total = 0
while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    total += numero
print(f"La suma total es: {total}")

# Actividad 5
print("\nActividad 5: Juego de adivinar un número")
numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivine el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Adivinaste en {intentos} intentos.")
        break

# Actividad 6
print("\nActividad 6: Números pares del 100 al 0")
for i in range(100, -1, -2):
    print(i)

# Actividad 7
print("\nActividad 7: Suma de números hasta un valor dado")
limite = int(input("Ingrese un número entero positivo: "))
suma = sum(range(limite + 1))
print(f"La suma de los números entre 0 y {limite} es: {suma}")

# Actividad 8
print("\nActividad 8: Clasificación de 100 números")
cantidad = 100  # Cambiar este valor para probar con menos números
pares = impares = positivos = negativos = 0
for _ in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

# Actividad 9
print("\nActividad 9: Media de 100 números")
cantidad = 100  # Cambiar este valor para probar con menos números
suma = 0
for _ in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    suma += numero
media = suma / cantidad
print(f"La media de los números ingresados es: {media}")

# Actividad 10
print("\nActividad 10: Invertir los dígitos de un número")
numero = input("Ingrese un número entero: ")
invertido = numero[::-1]
print(f"El número invertido es: {invertido}")