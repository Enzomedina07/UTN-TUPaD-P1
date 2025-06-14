# =================================================================
# TRABAJO PRÁCTICO 5: LISTAS
# Alumno: [Tu Nombre]
# Comisión: [Tu Comisión]
# =================================================================

print("--- Ejercicio 1: Múltiplos de 4 ---")
# Crear la lista de múltiplos de 4 del 1 al 100.
multiplos_cuatro = list(range(4, 101, 4))
print(multiplos_cuatro)
print("-" * 30)


print("--- Ejercicio 2: Penúltimo Elemento ---")
# Crear una lista con 5 elementos y mostrar el penúltimo.
mis_gustos = ["Leer", "Viajar", "Programar", "Café", "Música"]
penultimo = mis_gustos[-2]
print(f"Lista original: {mis_gustos}")
print(f"El penúltimo elemento es: {penultimo}")
print("-" * 30)


print("--- Ejercicio 3: Agregar a Lista Vacía ---")
# Crear una lista vacía y agregar tres palabras con append.
palabras = []
palabras.append("Hola")
palabras.append("Python")
palabras.append("UTN")
print(palabras)
print("-" * 30)


print("--- Ejercicio 4: Reemplazar Elementos en Lista ---")
# Reemplazar el segundo y último valor de la lista "animales".
animales = ["perro", "gato", "conejo", "pez"]
print(f"Lista original: {animales}")
animales[1] = "loro"
animales[-1] = "oso"
print(f"Lista modificada: {animales}")
print("-" * 30)


print("--- Ejercicio 5: Análisis de Programa ---")
# El código elimina el número más grande de la lista.
# 1. max(numeros) encuentra el valor 22.
# 2. numeros.remove(22) elimina ese valor de la lista.
numeros_ej5 = [8, 15, 3, 22, 7]
print(f"Lista original: {numeros_ej5}")
numeros_ej5.remove(max(numeros_ej5))
print(f"Lista sin el elemento mayor: {numeros_ej5}")
print("-" * 30)


print("--- Ejercicio 6: Saltos de 5 en 5 ---")
# Crear una lista con números del 10 al 30 (incluido), con saltos de 5.
numeros_ej6 = list(range(10, 31, 5))
print(f"Lista completa: {numeros_ej6}")
# Mostrar los dos primeros elementos usando slicing.
primeros_dos = numeros_ej6[:2]
print(f"Los dos primeros elementos son: {primeros_dos}")
print("-" * 30)


print("--- Ejercicio 7: Reemplazar Valores Centrales ---")
# Reemplazar los dos valores centrales (índices 1 y 2) de la lista.
autos = ["sedan", "polo", "suran", "gol"]
print(f"Lista original: {autos}")
autos[1:3] = ["onix", "cronos"]
print(f"Lista modificada: {autos}")
print("-" * 30)


print("--- Ejercicio 8: El Doble de un Número ---")
# Crear una lista vacía y agregar el doble de 5, 10 y 15.
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)
print("-" * 30)


print("--- Ejercicio 9: Manipular Lista Anidada 'compras' ---")
# Modificar una lista anidada según varias consignas.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print(f"Lista original de compras: {compras}")
# a) Agregar "jugo" al tercer cliente (índice 2)
compras[2].append("jugo")
# b) Reemplazar "fideos" por "tallarines"
compras[1][1] = "tallarines"
# c) Eliminar "pan" del primer cliente
compras[0].remove("pan")
print(f"Lista final de compras: {compras}")
print("-" * 30)


print("--- Ejercicio 10: Crear Lista Anidada ---")
# Elaborar una lista anidada con una estructura específica.
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print(lista_anidada)
print("-" * 30)