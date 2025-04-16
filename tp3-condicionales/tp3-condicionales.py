#Ejercicio 1:

edad = int(input("¿Cuántos años tenés? "))

if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")

#Ejercicio 2:

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

#Ejercicio 3:

print("Ingrese un número: ")
num = int(input())
if num % 2 == 0:
    print("El número", num, "es par.")
else:
    print("Por favor ingrese un número par.")

#Ejercicio 4:

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Eres un niño.")
elif edad >= 12 and edad < 18:
    print("Eres adolescente.")
elif edad >= 18 and edad < 30:
    print("Eres un adulto/a joven.")
else:
    print("Eres un adulto/a.")

#Ejercicio 5:

clave = input("Ingrese una contraseña entre 8 y 14 caracteres: ")
if 8 <= len(clave) <=14:
    print("Clave correcta.")
else:
    print("Por favor, ingrese una contraseña que contenga entre 8 y 14 caracteres.")

#Ejercicio 6:

import random
import statistics

num_aleatorios = [random.randint(1, 100) for i in range(50)]
print("Lista de número aleatorios: ")
print(num_aleatorios)
media = statistics.mean(num_aleatorios)
mediana = statistics.median(num_aleatorios)
moda = statistics.mode(num_aleatorios)
print(f"Media: {media}")
print(f"Mediana : {mediana}")
print(f"Moda: {moda}")

if media > mediana > moda:
    print("Distribución con sesgo positivo(a la derecha).")
elif media < mediana < moda:
    print("Distribución sos sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("Distribución sin sesgo.")
else:
    print("La distribución no cumple con ninguna de las condiciones exactas.")

#Ejercicio 7:

texto = input("Ingrese una frase o palabra: ")
if texto[-1].lower() in "aeiou":
    texto += "!"
    print("Resultado: ", texto)

#Ejercicio 8:

nombre = input("Ingrese su nombre: ")

print("Seleccione una opción:")
print("1. Mostrar el nombre en mayúsculas")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la primera letra en mayúscula")

opcion = input("Ingrese 1, 2 o 3: ")

if opcion == "1":
    print("Resultado:", nombre.upper())
elif opcion == "2":
    print("Resultado:", nombre.lower())
elif opcion == "3":
    print("Resultado:", nombre.title())
else:
    print("Opción no válida.")

#Ejercicio 9:

magnitud = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")


#Ejercicio 10:

hemisferio = input("¿En qué hemisferio te encuentras? (N para norte, S para sur): ").upper()
mes = int(input("Ingresa el mes del año (1-12): "))
dia = int(input("Ingresa el día del mes: "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
print(f"La estación del año es: {estacion}")