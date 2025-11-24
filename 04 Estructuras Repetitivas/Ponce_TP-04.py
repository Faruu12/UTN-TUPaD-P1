# ACTIVIDAD 1 #
for i in range(101):
    print(i)

# ACTIVIDAD 2 #
numero = input("Ingrese un numero entero: ")
print("Cantidad de digitos:", len(numero))

# ACTIVIDAD 3 #
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

if a > b:    # Si a es mayor que b, se intercambian

    aux = a
    a = b
    b = aux

suma = 0

for i in range(a + 1, b):
    suma += i

print("La suma es:", suma)

# ACTIVIDAD 4 #
suma = 0

while True:
    numero = int(input("Ingrese un numero para sumar (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print("La suma total es:", suma)

# ACTIVIDAD 5 #
import random

secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivine el número (0-9): "))
    intentos += 1

    if intento == secreto:
        print("¡Correcto! Lo lograste en", intentos, "intentos")
        break
# ACTIVIDAD 6 #
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)
# ACTIVIDAD 7 #
numero = int(input("Ingrese un numero entero positivo: "))

suma = 0
for i in range(numero + 1):
    suma += i

print("La suma es:", suma)

# ACTIVIDAD 8 #
cantidad = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    numero_usuario = int(input(f"Ingrese el número {i+1}: "))

    if numero_usuario % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero_usuario > 0:
        positivos += 1
    elif numero_usuario < 0:
        negativos += 1

print("\nResultados:")
print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# ACTIVIDAD 9 #
cantidad = 100
suma = 0

for i in range(cantidad):
    n = int(input(f"Ingrese el numero {i+1}: "))
    suma += n

media = suma / cantidad
print("La media es:", media)

# ACTIVIDAD 10 #
numero = input("Ingrese un numero: ")

invertido = ""

for i in range(len(numero) - 1, -1, -1):
    invertido += numero[i]

print("Numero invertido:", invertido)
