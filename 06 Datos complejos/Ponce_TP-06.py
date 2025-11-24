# ACTIVIDAD 1 # 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario después de agregar frutas:")
print(precios_frutas)

# ACTIVIDAD 2 #
precios_frutas['Banana'] = 1330 # Actualizar precios
precios_frutas['Manzana'] = 1700 # Actualizar precios
precios_frutas['Melón'] = 2800 # Actualizar precios

print("Diccionario con precios actualizados:")
print(precios_frutas)

# ACTIVIDAD 3 #
lista_frutas = list(precios_frutas.keys())

print("Lista de frutas:")
print(lista_frutas)

# ACTIVIDAD 4 #
agenda = {}

print("Carga 5 contactos:")
for i in range(5):
    nombre = input(f"Nombre del contacto {i+1}: ").strip()
    telefono = input(f"Telefono de {nombre}: ").strip()
    agenda[nombre] = telefono

contacto = input("Ingresa el nombre a consultar: ").strip()
if contacto in agenda:
    print(f"El telefono de {contacto} es: {agenda[contacto]}")
else:
    print(f"No existe un contacto llamado {contacto}.")

# ACTIVIDAD 5 #
frase = input("Ingresa una frase: ").strip()

palabras = [p.strip() for p in frase.lower().split() if p.strip()]

palabras_unicas = set(palabras)

conteo = {}
for p in palabras:
    conteo[p] = conteo.get(p, 0) + 1

print("Palabras unicas:")
print(palabras_unicas)
print("Conteo de cada palabra:")
print(conteo)

# ACTIVIDAD 6 #
alumnos = {}

print("Cargar 3 alumnos y sus 3 notas:")

for i in range(3):
    nombre = input("\nNombre del alumno: ")
    
    n1 = float(input("  Nota 1: "))
    n2 = float(input("  Nota 2: "))
    n3 = float(input("  Nota 3: "))

    alumnos[nombre] = (n1, n2, n3)

print("\nPromedios de cada alumno:")
for nombre in alumnos:
    notas = alumnos[nombre]
    promedio = (notas[0] + notas[1] + notas[2]) / 3
    print(nombre, "= Promedio:", promedio)

# ACTIVIDAD 7 #
parcial1 = {"Maria", "Pablo", "Jorge", "Marta", "Sergio"}
parcial2 = {"Pablo", "Marta", "Pedro", "Tomi", "Maria"}

ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:")
for alumno in ambos:
    print(alumno)

solo_uno = parcial1 ^ parcial2
print("\nAprobaron solo uno de los parciales:")
for alumno in solo_uno:
    print(alumno)

total = parcial1 | parcial2
print("\nAprobaron al menos un parcial:")
for alumno in total:
    print(alumno)

# ACTIVIDAD 8 #
stock = {
    "harina": 20,
    "azucar": 15,
    "yerba": 30,
    "leche": 12
}
producto = input("Ingrese el producto que desea consultar o modificar: ").lower()

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]} unidades")

    opcion = input("¿Desea agregar unidades al stock? (s/n): ").lower()

    if opcion == "s":
        cantidad = int(input("¿Cuantas unidades desea agregar?: "))
        stock[producto] += cantidad
        print(f"Stock actualizado de {producto}: {stock[producto]} unidades")

else:
    print("El producto no existe en el sistema.")
    agregar = input("¿Desea agregarlo como un producto nuevo? (s/n): ").lower()

    if agregar == "s":
        cantidad_inicial = int(input("Ingrese el stock inicial: "))
        stock[producto] = cantidad_inicial
        print(f"Producto agregado con exito. Stock de {producto}: {stock[producto]} unidades")

# Mostrar diccionario final
print("\nEstado final del stock:")
for prod, cant in stock.items():
    print(f"{prod}: {cant}")

# ACTIVIDAD 9 #
agenda = {}

print("Carga eventos en la agenda (dejar nombre vacío para terminar):")
while True:
    dia = input("  Dia (ej: Lunes): ").strip()
    if dia == "":
        break
    hora = input("  Hora (ej: 14:00): ").strip()
    evento = input("  Evento: ").strip()
    agenda[(dia, hora)] = evento
    print("  Evento guardado.\n")

consulta_dia = input("Consulta dia: ").strip()
consulta_hora = input("Consulta hora: ").strip()

evento = agenda.get((consulta_dia, consulta_hora))
if evento:
    print(f"En {consulta_dia} a las {consulta_hora} hay: {evento}")
else:
    print(f"No hay evento programado en {consulta_dia} a las {consulta_hora}.")

# ACTIVIDAD 10 #
paises_a_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Paraguay': 'Asuncion',
    'Uruguay': 'Montevideo'
}

# Construir el diccionario invertido
capitales_a_paises = {capital: pais for pais, capital in paises_a_capitales.items()}

print("Diccionario invertido (capital : pais):")
print(capitales_a_paises)
