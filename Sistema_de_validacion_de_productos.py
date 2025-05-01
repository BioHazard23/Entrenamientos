                                            #Sistema de validacion de productos.
                                            #Hecho por: Juan Manuel Arango Arana


import time #Para que haya un tiempo de espera en ciertos momentos antes de mostrar la informacion.
total_general = 0
lista_nombres = [] #Aqui se guardan los productos que el usuario ingrese.

#Se pide cuantos productos va a comprar.
num_productos = int(input("¿Cuantos productos vas a llevar?: "))

#Este bucle se repite de acuerdo al numero de productos que el usuari ingreso anteriormente.
for i in range(num_productos):
    print(f"\nProducto #{i + 1 }")

    #Entradas del usuario.
    nombre = input("Cual es el nombre del producto: ")
    precio = float(input("El precio unitario del producto es: "))
    cantidad = int(input("Que cantidad deseas llevar: "))
    descuento = float(input("Cual seria el porcentaje de descuento: "))

    #Verificacion para evitar errores.
    if precio <= 0:
        print ("Error: El precio debe ser mayor a cero.")
        continue
    if cantidad <= 0:
        print ("Error: La cantidad debe ser mayor a cero.")
        continue
    if (descuento < 0 or descuento > 100):
        print ("Error: el descuento debe estar en un rango de 0 a 100.")
        exit()
        continue
     
    lista_nombres.append (nombre) #Agrega el nombre del producto en la lista.

    total_sin_descuento = precio * cantidad #Muestra el total sin aplicar descuento.

    porcentaje_descuento = descuento / 100 * total_sin_descuento #Calculo del dinero que se descuenta.

    total_con_descuento = total_sin_descuento - porcentaje_descuento #Muestra el total ya con el descuento aplicado.

    total_general = total_general + total_con_descuento #Suma ese total a lo que seria el total final de la compra.

    #Se muestra un resumen del producto
    time.sleep (0.6)
    print (f"\nResumen de la compra: {nombre}")
    print (f"\nEl precio unitario es: {precio}")
    print (f"\nLa cantidad que vas a llevar seria: {cantidad} unidades")
    print (f"\nEl descuento aplicado es: {descuento}%")
    print (f"\nEl total de la compra sin descuento es: {total_sin_descuento:.3f}")
    print (f"\nEl descuento que se apico al producto {nombre} en tu compra es de: {porcentaje_descuento:.3f}")
    print (f"\nEl total de la compra con descuento es de: {total_con_descuento:.3f}")
    time.sleep (0.9)

#Muestra un resumen final al terminar la compra.
print ("\nResumen final de la compra:")
time.sleep (1.5)
print ("\nProductos ingresados:")
for nombre in lista_nombres:
    print (f"\n  -{nombre}")
time.sleep (2.2)
print (f"\nEl total a pagar por todos los productos que vas a llevar seria de: {total_general:.3f}")
print ("        Gracias por visitarnos, vualva pronto :)")