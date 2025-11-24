# ACTIVIDAD 1 #
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

numumero = int(input("Ingrese un numero para factorial: "))
for i in range(1, numumero + 1):
    print("Factorial de", i, "=", factorial(i))


# ACTIVIDAD 2 #
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

numero_fibonacci = int(input("\nPosicion de Fibonacci: "))
for i in range(numero_fibonacci + 1):
    print(fibonacci(i))


# ACTIVIDAD 3 #
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

b = int(input("\nBase: "))
e = int(input("Exponente: "))
print("Resultado:", potencia(b, e))


# ACTIVIDAD 4 #
def a_binario(numero):
    if numumero == 0:
        return "0"
    if numero == 1:
        return "1"
    return a_binario(numero // 2) + str(numero % 2)

num_bin = int(input("\nNumero para convertir a binario: "))
print("Binario:", a_binario(num_bin))


# ACTIVIDAD 5 #
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

pal = input("\nPalabra: ")
print(es_palindromo(pal))


# ACTIVIDAD 6 #
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

num_sd = int(input("\nNumero para sumar digitos: "))
print(suma_digitos(num_sd))


# ACTIVIDAD 7 #
def contar_bloques(numero):
    if numero == 1:
        return 1
    return numero + contar_bloques(numero - 1)

nivel = int(input("\nBloques en el nivel mas bajo: "))
print(contar_bloques(nivel))


# ACTIVIDAD 8 #
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

num_cd = int(input("\nNumero: "))
dig = int(input("Digito a buscar: "))
print(contar_digito(num_cd, dig))
