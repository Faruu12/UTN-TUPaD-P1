# ACTIVIDAD 1 #
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo() # Programa principal

# ACTIVIDAD 2 #
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ") # Programa principal
print(saludar_usuario(nombre))

# ACTIVIDAD 3 #
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Nombre: ") # Programa principal
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# ACTIVIDAD 4 #
def calcular_area_circulo(radio):
    pi = 3.14
    return pi * radio**2
def calcular_perimetro_circulo(radio):
    pi = 3.141592653589793
    return 2 * pi * radio

radio = float(input("Ingrese el radio del circulo: ")) # Programa principal

print("Area:", calcular_area_circulo(radio))
print("Perímetro:", calcular_perimetro_circulo(radio))

# ACTIVIDAD 5 #
def segundos_a_horas(segundos):
    return segundos / 3600

seg = float(input("Ingrese la cantidad de segundos: ")) # Programa principal
print("Equivalen a horas:", segundos_a_horas(seg))

# ACTIVIDAD 6 #
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num = int(input("Ingrese un numero para ver su tabla: ")) # Programa principal
tabla_multiplicar(num)

# ACTIVIDAD 7 #
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

a = float(input("Ingrese el primer numero: ")) # Programa principal
b = float(input("Ingrese el segundo numero: "))

resultados = operaciones_basicas(a, b)

print("Suma:", resultados[0])
print("Resta:", resultados[1])
print("Multiplicacion:", resultados[2])
print("Division:", resultados[3])

# ACTIVIDAD 8 #
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: ")) # Programa principal
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")

# ACTIVIDAD 9 #
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

celsius = float(input("Ingrese la temperatura en Celsius: ")) # Programa principal
print("Equivalente en Fahrenheit:", celsius_a_fahrenheit(celsius))

# ACTIVIDAD 10 #
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Primer número: "))# Programa principal
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))

print("El promedio es:", calcular_promedio(a, b, c))
