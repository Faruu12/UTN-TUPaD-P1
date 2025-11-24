import os
# 1. Crear archivo con productos (solo primera vez)
if not os.path.exists("productos.txt"):
    with open("productos.txt", "w") as f:
        f.write("Lapicera,120.5,30\n")
        f.write("Cuaderno,450.0,100\n")
        f.write("Regla,80.0,25\n")

# 2 y 4. Leer y cargar productos en lista de diccionarios
productos = []

with open("productos.txt", "r") as f:
    for linea in f:
        nombre, precio, cant = linea.strip().split(",")
        productos.append({"nombre": nombre, "precio": float(precio), "cantidad": int(cant)})
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cant}")

# 3. Agregar producto desde teclado
print()
nuevo_nombre = input("Ingrese nombre del producto: ")
nuevo_precio = input("Ingrese precio: ")
nueva_cant = input("Ingrese cantidad: ")

with open("productos.txt", "a") as f:
    f.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cant}\n")

productos.append({
    "nombre": nuevo_nombre,
    "precio": float(nuevo_precio),
    "cantidad": int(nueva_cant)
})
# 5. Buscar producto por nombre
buscar = input("\nBuscar producto: ")
encontrado = False

for prod in productos:
    if prod["nombre"].lower() == buscar.lower():
        print("Encontrado:", prod)
        encontrado = True
        break

if not encontrado:
    print("No existe.")

# 6. Guardar archivo sobrescribiendo todo
with open("productos.txt", "w") as f:
    for prod in productos:
        f.write(f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n")
