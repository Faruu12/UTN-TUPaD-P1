#ejercicio 1

print ("Hola Mundo")

#ejercicio 2

nombre = input("Por favor, ingresa tu nombre: ")
print(f"Hola {nombre}!")

#ejercicio 3

nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Por favor, ingresa tu apellido: ")
edad = input("Por favor, ingresa tu edad: ")
residencia = input("Por favor, ingresa tu pais de residencia: ")
print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia} ")

#ejercicio 4

radio = float(input("Por favor, ingresa el radio del círculo: "))
area = 3.1416 * radio ** 2
perimetro = 2 * 3.1416 * radio
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")


#ejercicio 5

segundos = float(input ("Por ingresa los segundos "))
horas = segundos / 3600
print(f"Los {segundos} segundos en Horas serian {horas}")

#ejercicio 6

numero = int(input("Por ingresa un numero entero "))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#ejercicio 7

numero = int(input("Por ingresa un numero entero distinto que cero "))
numero2 = int(input("Por ingresa otro numero entero distinto que cero "))
print(f"Suma = {numero + numero2}")
print(f"Division = {numero / numero2}")
print(f"Multiplicacion = {numero * numero2}")
print(f"Resta {numero - numero2}")

#ejercicio 8

peso = float(input("Por ingresa su peso en KG "))
altura = float(input("Por ingresa su altura en M "))
imc = peso / (altura * altura)
print(f"su masa corporal es {imc}")

#ejercicio 9    

celsius = float(input("Por ingresa una temperatura en grados Celsius "))
fahrenheit = 1.8 * celsius + 32 
print(f"los grados en fahrenheit es {fahrenheit}") 

#ejercicio 10
    
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio:}")
