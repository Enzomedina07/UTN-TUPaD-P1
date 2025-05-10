#ejercicio 1
edad = int(input("cuantos anios tienes? "))
if edad >= 18:
    print("Es mayor de edad")
#ejercicio 2
nota = int(input("cuanto sacaste en el examen? "))
if nota >= 6:
    print("Aprobado")
else:
    print("Reprobado")
#ejercicio 3
numero = int(input("ingrese un numero par: "))
if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar") 
#ejercicio 4
edadd = int(input("cuantos anios tienes? "))
if edadd >= 12 and edadd <= 18:
    print("Es adolescente")
elif edadd >= 18 and edadd <= 30:
    print("Es joven")
elif edadd >= 30:
    print("Es adulto")
else :
    print("Es niño")
#ejercicio 5
contrasena = input("ingrese la contrasena (entre 8 y 14 caracteres): ")
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Contrasena valida")
else:
    print("Por favor ingrese entre 8 y 14 caracteres")
#ejercicio 6
from statistics import mode, median, mean
mi_lista = [1,2,5,5,3]
mean(mi_lista)
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print("La media es: ", mean(numeros_aleatorios))
print("La moda es: ", mode(numeros_aleatorios))
print("La mediana es: ", median(numeros_aleatorios))
#ejercicio 7
frase = input("ingrese una frase: ")
vocales = "aeiou"  
for letra in frase:
    if letra.lower() in vocales:
        frase = frase.replace(letra, letra.upper())
    print(frase + "!")
else:
    print(frase)
#ejercicio 8
nombre = input("ingrese su nombre: ")
opcion = input("1 Si quiere su nombre en Mayus, 2 Si quiere su nombre en minuscula y 3 si quiere su nombre con la primera letrra mayuscula. Ingrese la opcion deseada: ")
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.capitalize())
#ejercicio 9
#Progrma que pida al usuario la magnitud de un terremoto y clasifique en las siquientes categorias:
#menor que 3 muy leve
#mayor o igual que 3 y menos que 4 leve
#mayor o igual que 4 y menos que 5 moderado
#mayor o igual que 5 y menos que 6 fuerte  
#mayor o igual que 6 y menos que 7 muy fuerte
#mayor o igual que 7 extremo
magnitud = float(input("ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print("muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("leve")
elif magnitud >= 4 and magnitud < 5:
    print("moderado")
elif magnitud >= 5 and magnitud < 6:
    print("fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("muy fuerte")
elif magnitud >= 7:
    print("extremo")
#ejercicio 10
#programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("en que hemisferio se encuentra? (N/S): ")
mes = int(input("que mes es? (1-12): "))   
dia = int(input("que dia es? (1-31): "))
if hemisferio == "N":
    if mes == 3 and dia >= 20 or mes == 4 or mes == 5 or mes == 6 and dia < 21:
        print("otoño")
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia < 23:
        print("invierno")
    elif mes == 9 and dia >= 23 or mes == 10 or mes == 11 or mes == 12 and dia < 21:
        print("primavera")
    elif mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia < 20:
        print("verano")
elif hemisferio == "S":
    if mes == 3 and dia >= 20 or mes == 4 or mes == 5 or mes == 6 and dia < 21:
        print("verano")
    elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia < 23:
        print("otoño")
    elif mes == 9 and dia >= 23 or mes == 10 or mes == 11 or mes == 12 and dia < 21:
        print("invierno")
    elif mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia < 20:
        print("primavera")



