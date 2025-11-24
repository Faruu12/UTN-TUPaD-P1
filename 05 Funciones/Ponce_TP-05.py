# ACTIVIDAD 1 #
notas = [7, 5, 9, 4, 8, 6, 10, 3, 7, 9]

print("Notas de los estudiantes:")
for n in notas:
    print(n)

promedio = sum(notas) / len(notas)
print("Promedio:", promedio)
print("Nota mas alta:", max(notas))
print("Nota mas baja:", min(notas))

# ACTIVIDAD 2 #
productos = []

for i in range(5):
    p = input(f"Ingrese el producto {i+1}: ")
    productos.append(p)

print("\nLista ordenada alfabéticamente:")
ordenada = sorted(productos)
for p in ordenada:
    print(p)

eliminar = input("\n¿Que producto desea eliminar?: ")

if eliminar in productos:
    productos.remove(eliminar)
    print("Producto eliminado.")
else:
    print("Ese producto no esta en la lista.")

print("\nLista actualizada:")
for p in productos:
    print(p)

# ACTIVIDAD 3 #
import random

numeros = [random.randint(1, 100) for i in range(15)]
pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))

# ACTIVIDAD 4 #
lista = [4, 2, 7, 2, 9, 4, 1, 7]
sin_repetidos = []

for n in lista:
    if n not in sin_repetidos:
        sin_repetidos.append(n)

print("Lista sin repetidos:")
for n in sin_repetidos:
    print(n)

# ACTIVIDAD 5 #
estudiantes = ["Axel", "Luis", "Pablo", "Juan", "Sofía", "Pedro", "Leo", "Julian"]

operacion = input("¿Desea agregar (A) o eliminar (E) un estudiante?: ").upper()

if operacion == "A":
    nuevo = input("Ingrese el nombre del estudiante a agregar: ")
    estudiantes.append(nuevo)

elif operacion == "E":
    borrar = input("Ingrese el nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
    else:
        print("Ese estudiante no está en la lista.")

print("\nLista final:")
for e in estudiantes:
    print(e)

# ACTIVIDAD 6 #
lista = [5, 12, 7, 3, 9, 1, 8]

ultimo = lista[-1]

for i in range(len(lista) - 1, 0, -1):
    lista[i] = lista[i - 1]

lista[0] = ultimo

print("Lista rotada:")
for n in lista:
    print(n)

# ACTIVIDAD 7 #
temp = [
    [12, 20], # [min, max]
    [10, 22],
    [14, 25],
    [13, 21],
    [9, 19],
    [11, 24],
    [15, 27],
]
suma_min = 0
suma_max = 0
mayor_amplitud = -1
dia_amplitud = 0

for i in range(7):
    minima = temp[i][0]
    maxima = temp[i][1]

    suma_min += minima
    suma_max += maxima

    amplitud = maxima - minima
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_amplitud = i + 1

print("Promedio mínimas:", suma_min / 7)
print("Promedio máximas:", suma_max / 7)
print("Mayor amplitud térmica en el día:", dia_amplitud)

# ACTIVIDAD 8 #
notas = [
    [7, 5, 6],
    [8, 9, 7],
    [6, 4, 5],
    [10, 8, 9],
    [5, 6, 7]
]

# Promedio por estudiante
for i in range(5):
    promedio = sum(notas[i]) / 3
    print(f"Promedio del estudiante {i+1}: {promedio}")

# Promedio por materia
for m in range(3):
    suma = 0
    for e in range(5):
        suma += notas[e][m]
    print(f"Promedio de la materia {m+1}: {suma / 5}")

# ACTIVIDAD 9 #
# tablero vacío
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))
    print()

def pedir_jugada(jugador):
    while True:
        print(f"Turno del jugador {jugador}")
        fila = int(input("Ingrese la fila (0-2): "))
        columna = int(input("Ingrese la columna (0-2): "))

        # Validar que esté dentro del rango
        if fila < 0 or fila > 2 or columna < 0 or columna > 2:
            print("Posición fuera del tablero. Intente nuevamente.\n")
            continue

        # Validar que esté libre
        if tablero[fila][columna] != "-":
            print("Casilla ocupada. Intente otra.\n")
            continue
        
        return fila, columna

# Mostrar tablero vacío al inicio
mostrar_tablero()

# 9 turnos máximo
for turno in range(9):
    jugador = "X" if turno % 2 == 0 else "O"
    
    fila, columna = pedir_jugada(jugador)
    tablero[fila][columna] = jugador

    mostrar_tablero()

# ACTIVIDAD 10 #
ventas = [
    [10, 12, 8, 9, 7, 11, 15],
    [5, 7, 6, 8, 9, 10, 12],
    [9, 10, 12, 11, 14, 13, 16],
    [4, 6, 5, 7, 6, 8, 9]
]

# Total por producto
for p in range(4):
    total = sum(ventas[p])
    print(f"Producto {p+1} vendido en total:", total)

# Día con mayores ventas
mayor_dia = 0
max_total = -1

for d in range(7):
    suma_dia = 0
    for p in range(4):
        suma_dia += ventas[p][d]
    if suma_dia > max_total:
        max_total = suma_dia
        mayor_dia = d + 1

print("Día con mayores ventas totales:", mayor_dia)

# Producto más vendido
totales_productos = [sum(ventas[p]) for p in range(4)]
producto_max = totales_productos.index(max(totales_productos)) + 1

print("Producto más vendido en la semana:", producto_max)

