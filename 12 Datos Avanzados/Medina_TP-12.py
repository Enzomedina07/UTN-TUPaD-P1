# TP 6: Estructuras de Datos Complejas

# Ejercicio 1: Añadir elementos a un diccionario
def ejercicio_1():
    print("\n--- Ejercicio 1: Añadir elementos al diccionario ---")
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    print(f"Diccionario inicial: {precios_frutas}")

    # Añadir nuevas frutas con sus precios
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300

    print(f"Diccionario después de añadir: {precios_frutas}")
    return precios_frutas # Retornamos el diccionario modificado para el siguiente ejercicio

# Ejercicio 2: Actualizar precios en el diccionario
def ejercicio_2(precios_frutas):
    print("\n--- Ejercicio 2: Actualizar precios en el diccionario ---")
    print(f"Diccionario antes de actualizar: {precios_frutas}")

    # Actualizar precios de frutas existentes
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800

    print(f"Diccionario después de actualizar: {precios_frutas}")
    return precios_frutas # Retornamos el diccionario modificado

# Ejercicio 3: Crear una lista de frutas sin precios
def ejercicio_3(precios_frutas):
    print("\n--- Ejercicio 3: Crear lista de frutas ---")
    print(f"Diccionario base: {precios_frutas}")

    # Obtener solo las claves (nombres de las frutas) y convertirlas a lista
    lista_frutas = list(precios_frutas.keys())

    print(f"Lista de frutas (solo nombres): {lista_frutas}")
    return lista_frutas

# Ejercicio 4: Almacenar y consultar números telefónicos 
def ejercicio_4():
    print("\n--- Ejercicio 4: Agenda telefónica simple ---")
    contactos = {}

    # Permitir al usuario cargar 5 contactos 
    print("Por favor, carga 5 contactos (nombre y número):")
    for i in range(5):
        nombre = input(f"Ingresa el nombre del contacto {i+1}: ")
        numero = input(f"Ingresa el número de teléfono de {nombre}: ")
        contactos[nombre] = numero
    
    print(f"\nContactos cargados: {contactos}")

    # Pedir un nombre y mostrar el número asociado 
    while True:
        nombre_consulta = input("\nIngresa el nombre del contacto a consultar (o 'salir' para terminar): ")
        if nombre_consulta.lower() == 'salir':
            break
        
        if nombre_consulta in contactos:
            print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
        else:
            print(f"El contacto '{nombre_consulta}' no se encuentra en la agenda.")

# Ejercicio 5: Analizar frase (palabras únicas y frecuencia) 
def ejercicio_5():
    print("\n--- Ejercicio 5: Análisis de frase ---")
    frase = input("Ingresa una frase: ").lower() # Convertir a minúsculas para un conteo no sensible a mayúsculas/minúsculas

    # Separar la frase en palabras
    palabras = frase.split()

    # Las palabras únicas (usando un set) 
    palabras_unicas = set(palabras)
    print(f"Palabras únicas: {palabras_unicas}")

    # Un diccionario con la cantidad de veces que aparece cada palabra 
    recuento_palabras = {}
    for palabra in palabras:
        recuento_palabras[palabra] = recuento_palabras.get(palabra, 0) + 1
    
    print(f"Recuento de palabras: {recuento_palabras}")

# Ejercicio 6: Promedio de notas de alumnos 
def ejercicio_6():
    print("\n--- Ejercicio 6: Promedio de notas de alumnos ---")
    alumnos = {}

    # Permitir ingresar nombres de 3 alumnos y 3 notas para cada uno 
    for i in range(3):
        nombre_alumno = input(f"Ingresa el nombre del alumno {i+1}: ")
        
        notas_str = input(f"Ingresa 3 notas para {nombre_alumno} separadas por comas (ej: 10,9,8): ")
        try:
            # Convertir las notas a enteros y almacenarlas en una tupla
            notas = tuple(map(int, notas_str.split(',')))
            if len(notas) != 3:
                print("Debes ingresar exactamente 3 notas. Inténtalo de nuevo.")
                continue # Volver a pedir las notas para este alumno
            alumnos[nombre_alumno] = notas
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar números separados por comas.")
            continue # Volver a pedir las notas para este alumno
    
    print(f"\nAlumnos y sus notas: {alumnos}")

    # Mostrar el promedio de cada alumno 
    print("\n--- Promedio de cada alumno ---")
    for alumno, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"El promedio de {alumno} es: {promedio:.2f}") # Formatear a 2 decimales

# Ejercicio 7: Operaciones con sets de estudiantes 
def ejercicio_7():
    print("\n--- Ejercicio 7: Operaciones con sets de estudiantes ---")
    aprobados_parcial1 = {"Juan", "María", "Pedro", "Ana", "Luis"}
    aprobados_parcial2 = {"Pedro", "Ana", "Sofía", "Carlos", "María"}

    print(f"Aprobados Parcial 1: {aprobados_parcial1}")
    print(f"Aprobados Parcial 2: {aprobados_parcial2}")

    # Mostrar los que aprobaron ambos parciales (intersección) 
    ambos_parciales = aprobados_parcial1.intersection(aprobados_parcial2)
    print(f"\nEstudiantes que aprobaron ambos parciales: {ambos_parciales}")

    # Mostrar los que aprobaron solo uno de los dos (diferencia simétrica) 
    solo_uno_parcial = aprobados_parcial1.symmetric_difference(aprobados_parcial2)
    print(f"Estudiantes que aprobaron solo uno de los dos parciales: {solo_uno_parcial}")

    # Mostrar la lista total de estudiantes que aprobaron al menos un parcial (unión) 
    total_aprobados = aprobados_parcial1.union(aprobados_parcial2)
    print(f"Lista total de estudiantes que aprobaron al menos un parcial: {total_aprobados}")

# Ejercicio 8: Gestión de stock de productos 
def ejercicio_8():
    print("\n--- Ejercicio 8: Gestión de stock de productos ---")
    stock_productos = {
        "camisa": 50,
        "pantalon": 30,
        "zapatillas": 20
    }
    print(f"Stock inicial: {stock_productos}")

    while True:
        print("\nOpciones:")
        print("1. Consultar stock de un producto")
        print("2. Agregar unidades a un producto existente")
        print("3. Agregar un nuevo producto")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            producto = input("Ingresa el nombre del producto a consultar: ").lower()
            if producto in stock_productos:
                print(f"El stock de {producto} es: {stock_productos[producto]} unidades.")
            else:
                print(f"El producto '{producto}' no se encuentra en el stock.")
        
        elif opcion == '2':
            producto = input("Ingresa el nombre del producto al que quieres agregar unidades: ").lower()
            if producto in stock_productos:
                try:
                    cantidad = int(input(f"¿Cuántas unidades deseas agregar a {producto}?: "))
                    if cantidad > 0:
                        stock_productos[producto] += cantidad
                        print(f"Se agregaron {cantidad} unidades. Nuevo stock de {producto}: {stock_productos[producto]}.")
                    else:
                        print("La cantidad a agregar debe ser mayor que cero.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número entero.")
            else:
                print(f"El producto '{producto}' no existe. Usa la opción 3 para agregarlo.")
        
        elif opcion == '3':
            producto = input("Ingresa el nombre del nuevo producto: ").lower()
            if producto in stock_productos:
                print(f"El producto '{producto}' ya existe. Usa la opción 2 para agregar unidades.")
            else:
                try:
                    cantidad = int(input(f"Ingresa el stock inicial para {producto}: "))
                    if cantidad >= 0:
                        stock_productos[producto] = cantidad
                        print(f"Producto '{producto}' agregado con stock inicial de {cantidad}.")
                    else:
                        print("El stock inicial no puede ser negativo.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número entero.")

        elif opcion == '4':
            print("Saliendo de la gestión de stock.")
            break
        
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
        
        print(f"Stock actual: {stock_productos}")

# Ejercicio 9: Agenda con tuplas como claves 
def ejercicio_9():
    print("\n--- Ejercicio 9: Agenda de eventos ---")
    agenda = {
        ("lunes", "10:00"): "Reunión",
        ("martes", "15:00"): "Clase de inglés",
        ("miércoles", "09:30"): "Cita con el dentista"
    }
    print(f"Agenda actual: {agenda}")

    while True:
        print("\nOpciones:")
        print("1. Consultar actividad en un día y hora específicos")
        print("2. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            dia = input("Ingresa el día (ej: lunes): ").lower()
            hora = input("Ingresa la hora (ej: 10:00): ")
            
            clave_consulta = (dia, hora)
            
            if clave_consulta in agenda:
                print(f"Actividad para {dia} a las {hora}: {agenda[clave_consulta]}")
            else:
                print(f"No hay actividad programada para {dia} a las {hora}.")
        
        elif opcion == '2':
            print("Saliendo de la agenda.")
            break
        
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejercicio 10: Invertir diccionario (claves por valores y viceversa) 
def ejercicio_10():
    print("\n--- Ejercicio 10: Invertir diccionario ---")
    original_paises_capitales = {"Argentina": "Buenos Aires", "Chile": "Santiago", "España": "Madrid"}
    print(f"Diccionario original: {original_paises_capitales}")

    # Construir un nuevo diccionario donde las capitales sean las claves y los países los valores 
    invertido_capitales_paises = {valor: clave for clave, valor in original_paises_capitales.items()}

    print(f"Diccionario invertido: {invertido_capitales_paises}")

# Función principal para ejecutar todos los ejercicios
def main():
    print("--- Bienvenido al TP 6: Estructuras de Datos Complejas ---")

    # Ejecutar Ejercicio 1
    precios_frutas_modificado_1 = ejercicio_1()

    # Ejecutar Ejercicio 2 (usa el resultado del Ejercicio 1)
    precios_frutas_modificado_2 = ejercicio_2(precios_frutas_modificado_1)

    # Ejecutar Ejercicio 3 (usa el resultado del Ejercicio 2)
    ejercicio_3(precios_frutas_modificado_2)

    # Ejecutar Ejercicio 4
    ejercicio_4()

    # Ejecutar Ejercicio 5
    ejercicio_5()

    # Ejecutar Ejercicio 6
    ejercicio_6()

    # Ejecutar Ejercicio 7
    ejercicio_7()

    # Ejecutar Ejercicio 8
    ejercicio_8()

    # Ejecutar Ejercicio 9
    ejercicio_9()

    # Ejecutar Ejercicio 10
    ejercicio_10()

    print("\n--- Fin del TP 6 ---")

if __name__ == "__main__":
    main()