# --- Definición de Funciones Recursivas ---

# Ejercicio 1: Factorial de un número
def factorial(n):
    """Calcula el factorial de n de forma recursiva."""
    # Caso base: el factorial de 0 es 1.
    if n == 0:
        return 1
    # Paso recursivo: n * factorial(n-1)
    else:
        return n * factorial(n - 1)

# Ejercicio 2: Sucesión de Fibonacci
def fibonacci(pos):
    """Calcula el número de Fibonacci en una posición dada."""
    # Caso base 1: F(0) = 0
    if pos == 0:
        return 0
    # Caso base 2: F(1) = 1
    elif pos == 1:
        return 1
    # Paso recursivo: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

# Ejercicio 3: Potencia de un número
def potencia(base, exponente):
    """Calcula la potencia de un número de forma recursiva."""
    # Caso base: cualquier número elevado a 0 es 1.
    if exponente == 0:
        return 1
    # Paso recursivo: n^m = n * n^(m-1)
    else:
        return base * potencia(base, exponente - 1)

# Ejercicio 4: Conversión de decimal a binario
def decimal_a_binario(n):
    """Convierte un número decimal a su representación binaria como string."""
    # Caso base: la conversión de 0 es "0".
    if n == 0:
        return "0"
    # Se usa un sub-algoritmo para no tener ceros a la izquierda en el resultado final
    elif n < 0:
        return "No se pueden convertir números negativos."

    def binario_recursivo(num):
        # Caso base del sub-algoritmo
        if num == 0:
            return ""
        # Paso recursivo: se concatena el resultado de la división entera con el resto
        else:
            return binario_recursivo(num // 2) + str(num % 2)

    return binario_recursivo(n)

# Ejercicio 5: Verificador de palíndromos
def es_palindromo(palabra):
    """Verifica si una palabra es un palíndromo de forma recursiva."""
    # Quitar espacios y convertir a minúsculas para una comparación robusta
    palabra = palabra.lower().replace(" ", "")
    # Caso base: una palabra con 0 o 1 letra es un palíndromo.
    if len(palabra) <= 1:
        return True
    # Paso recursivo: si la primera y última letra son iguales,
    # se verifica el resto de la palabra.
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    # Si no son iguales, no es un palíndromo.
    else:
        return False

# Ejercicio 6: Suma de dígitos de un número
def suma_digitos(n):
    """Suma los dígitos de un número entero positivo de forma recursiva."""
    # Caso base: si el número tiene un solo dígito, la suma es el propio número.
    if n < 10:
        return n
    # Paso recursivo: suma el último dígito (n % 10) con la suma
    # de los dígitos restantes (n // 10).
    else:
        return (n % 10) + suma_digitos(n // 10)

# Ejercicio 7: Conteo de bloques de una pirámide
def contar_bloques(n):
    """Calcula el total de bloques en una pirámide de n niveles."""
    # Caso base: una pirámide de 1 nivel tiene 1 bloque.
    if n <= 1:
        return n
    # Paso recursivo: n + el total de bloques para una pirámide de n-1 niveles.
    else:
        return n + contar_bloques(n - 1)

# Ejercicio 8: Conteo de un dígito específico en un número
def contar_digito(numero, digito):
    """Cuenta cuántas veces aparece un dígito en un número."""
    # Caso base: si el número es 0, no hay más dígitos que contar.
    if numero == 0:
        return 0
    # Paso recursivo
    else:
        # Se verifica si el último dígito es el que buscamos
        if numero % 10 == digito:
            # Si es, contamos 1 y seguimos con el resto del número
            return 1 + contar_digito(numero // 10, digito)
        else:
            # Si no es, seguimos con el resto del número sin contar
            return contar_digito(numero // 10, digito)

# --- Programa Principal ---
if __name__ == "__main__":
    print("### EJERCICIO 1: Factorial ###")
    num_fact = int(input("Ingrese un número para calcular factoriales hasta él: "))
    for i in range(1, num_fact + 1):
        print(f"El factorial de {i} es {factorial(i)}")
    print("-" * 30)

    print("### EJERCICIO 2: Fibonacci ###")
    pos_fib = int(input("Ingrese una posición para ver la serie de Fibonacci: "))
    print("La serie de Fibonacci es: ", end="")
    for i in range(pos_fib + 1):
        print(fibonacci(i), end=" ")
    print("\n" + "-" * 30)

    print("### EJERCICIO 3: Potencia ###")
    base_pot = int(input("Ingrese el número base: "))
    exp_pot = int(input("Ingrese el exponente: "))
    print(f"{base_pot} elevado a {exp_pot} es {potencia(base_pot, exp_pot)}")
    print("-" * 30)

    print("### EJERCICIO 4: Decimal a Binario ###")
    num_dec = int(input("Ingrese un número decimal para convertir a binario: "))
    print(f"El número {num_dec} en binario es {decimal_a_binario(num_dec)}")
    print("-" * 30)

    print("### EJERCICIO 5: Palíndromo ###")
    palabra_pal = input("Ingrese una palabra para verificar si es un palíndromo: ")
    if es_palindromo(palabra_pal):
        print(f"'{palabra_pal}' SÍ es un palíndromo.")
    else:
        print(f"'{palabra_pal}' NO es un palíndromo.")
    print("-" * 30)

    print("### EJERCICIO 6: Suma de Dígitos ###")
    num_sum = int(input("Ingrese un número para sumar sus dígitos: "))
    print(f"La suma de los dígitos de {num_sum} es {suma_digitos(num_sum)}")
    print("-" * 30)

    print("### EJERCICIO 7: Pirámide de Bloques ###")
    niveles_piramide = int(input("Ingrese el número de bloques en la base de la pirámide: "))
    print(f"El total de bloques para la pirámide es {contar_bloques(niveles_piramide)}")
    print("-" * 30)

    print("### EJERCICIO 8: Contar Dígito ###")
    num_contar = int(input("Ingrese un número entero positivo: "))
    dig_contar = int(input("Ingrese el dígito (0-9) que desea contar: "))
    print(f"El dígito {dig_contar} aparece {contar_digito(num_contar, dig_contar)} veces en {num_contar}.")
    print("-" * 30)