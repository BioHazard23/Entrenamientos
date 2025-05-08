#Gestion de inventario
inventario={}

#Añadir Productos
def añadir_producto(nombre, precio, cantidad):
    if nombre in inventario:
     print("El producto ya existe.")
    else:
       inventario[nombre] = (precio, cantidad)

#Consultar Productos
def consultar_producto(nombre):
   if nombre in inventario:
      precio, cantidad = inventario[nombre]
      print(f"El precio es {precio:.3f} y la cantidad que hay es {cantidad} unidades.")
   else:
      print("Producto no encontrado.")
    
#Actualizar Precios
def actualizar_precio(nombre, nuevo_precio):
   if nombre in inventario:
      _, cantidad = inventario[nombre]
      inventario[nombre]=(nuevo_precio, cantidad)
   else:
      print("El producto no existe.")

#Eliminar Producto
def eliminar_producto(nombre):
   if nombre in inventario:
      del inventario[nombre]
      print("Producto eliminado.")
   else:
      print("El producto no existe.")

#Calcular valor del inventario
def calcular_valor_inventario():
    calcular = lambda: sum(precio * cantidad for precio, cantidad in inventario.values())
    return calcular()

#Menu Interactivo
def menu():
   while True:
    print("----------MENU----------")
    print("\n 1. Añadir Producto.")
    print(" 2. Consultar Producto.")
    print(" 3. Actualizar Precio.")
    print(" 4. Eliminar Producto.")
    print(" 5. Calcular Valor Total Del Inventario.")
    print(" 6. Salir.")

    opcion = input("\nSelecciona una de las anteriores opciones: ")

    if opcion == "1":
       nombre = input("Nombre: ")
       try:
          precio=float(input("Precio: "))
          cantidad=int(input("Cantidad: "))
          añadir_producto (nombre, precio, cantidad)
       except ValueError:
          print("Dato invalido.")
    
    elif opcion == "2":
       nombre=input("Nombre:")
       consultar_producto(nombre)

    elif opcion == "3":
       nombre = input("Nombre: ")
       try:
          nuevo_precio=float(input("Nuevo precio: "))
          actualizar_precio(nombre, nuevo_precio)
       except ValueError:
          print("Dato invalido.")
    
    elif opcion == "4":
       nombre=input("Nombre: ")
       eliminar_producto(nombre)
    
    elif opcion == "5":
       print(f"El valor total del inventario es: {calcular_valor_inventario():.3f}")
    
    elif opcion == "6":
       print("¡Hasta Luego!")
       break
    
    else:
       print("Opcion invalida")
       
#Muestra Las Opciones
menu()


   