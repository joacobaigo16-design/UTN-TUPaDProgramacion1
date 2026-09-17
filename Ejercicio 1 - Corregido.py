#pedir nombre del cliente
nombre = input("Cliente: ")

while not nombre.isalpha():
    print("Error: ingrese un nombre válido.")
    nombre = input("Cliente: ")


#pedir cantidad de productos
cantidad = input("Cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: ingrese una cantidad válida mayor a 0.")
    cantidad = input("Cantidad de productos: ")

cantidad = int(cantidad)


#variables para los totales
total_sin_descuentos = 0
total_con_descuentos = 0


#pedir datos de cada producto
for i in range(1, cantidad + 1):

    precio = input(f"Producto {i} - Precio: ")

    while not precio.isdigit():
        print("Error: ingrese un precio válido.")
        precio = input(f"Producto {i} - Precio: ")

    precio = int(precio)

    descuento = input("Descuento (S/N): ")

    while descuento.lower() != "s" and descuento.lower() != "n":
        print("Error: ingrese S o N.")
        descuento = input("Descuento (S/N): ")

    #sumar al total sin descuentos
    total_sin_descuentos += precio

    #aplicar descuento si corresponde
    if descuento.lower() == "s":
        precio_con_descuento = precio * 0.90
    else:
        precio_con_descuento = precio

    total_con_descuentos += precio_con_descuento


#calculo del ahorro
ahorro = total_sin_descuentos - total_con_descuentos

#calculo del promedio
promedio = total_con_descuentos / cantidad
promedio = float(promedio)


#mostrar resultados
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

