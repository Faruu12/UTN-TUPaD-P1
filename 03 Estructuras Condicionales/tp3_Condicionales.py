# ACTIVIDAD 1 #
edad = int(input("Ingrese su edad: "))

if edad > 18:
 print("Es mayor de edad")

# ACTIVIDAD 2 #
nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# ACTIVIDAD 3 #
numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# ACTIVIDAD 4 #
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad < 18:
    print("Adolescente")
elif edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# ACTICIDAD 6 #

import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
else:
    print("Sin sesgo")

# ACTICIDAD 7 #

texto = input("Ingrese una palabra o frase: ")

if texto[-1].lower() in "aeiou":
    texto = texto + "!"

print(texto)

# ACTICIDAD 8 #

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 (MAYÚSCULAS), 2 (minúsculas) o 3 (Primer letra mayúscula): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción no válida")

# ACTICIDAD 9 #

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (puede no causar daños)")
elif magnitud < 6:
    print("Fuerte (daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy fuerte (daños significativos)")
else:
    print("Extremo (graves daños a gran escala)")

# ACTICIDAD 10 #

hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

if mes == 12 and dia >= 21 or mes in [1, 2] or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"

elif mes == 3 and dia >= 21 or mes in [4, 5] or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"

elif mes == 6 and dia >= 21 or mes in [7, 8] or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"

else:
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

if hemisferio == "N":
    print("Estación:", estacion_norte)
elif hemisferio == "S":
    print("Estación:", estacion_sur)
else:
    print("Hemisferio inválido")


