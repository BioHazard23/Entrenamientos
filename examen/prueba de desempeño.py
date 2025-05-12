                                                        #Prueba Desempeño - Modulo 1
                                                         #Juan Manuel Arango Arana.

import time

#Colors
DANGER = "\033[91m"
SUCCESS = "\033[92m"
WARNING = "\033[93m"
EXIT = "\033[95m"
TITLE = "\033[96m"
RESET = "\033[0m"



#Beginning Inventory
inventory = {}


#Add Productos To Inventory          
def add_products ():
    time.sleep (0.2)
    print(TITLE + "\n----------Añadir Productos----------" + RESET)
    time.sleep (0.4)
    name = input("Ingresa el nombre del producto: ")
    if name in inventory:
        print(DANGER + "El producto ya se encuentra registrado." + RESET)
        return
    try:
        time.sleep (0.2)
        price = float(input("Ingresa el precio del producto: "))
        time.sleep (0.2)
        quantity = int(input("Ingresa la cantidad: "))
        if price <= 0 or quantity < 0:
            print(DANGER + "El valor debe ser positivo." + RESET)
            return
        inventory[name] = {"price": price, "quantity": quantity}
        time.sleep (0.6)
        print(SUCCESS + ("El producto se agrego correctamente." + RESET))

    except ValueError:
        time.sleep (0.2)
        print(DANGER + "El precio debe ser un un numero y la cantidad un numero entero" + RESET)

#Check Products In Inventory
def check_products ():
    time.sleep (0.2)
    print(TITLE + "\n----------Consultar Productos----------" + RESET)
    time.sleep (0.4)
    name = input("Ingresa un producto para buscar: ")
    if name in inventory:
        time.sleep (0.3)
        print(f"producto: {name}")
        print(f"Precio: $ {inventory[name]['price']:.3f}")
        print(f"Cantidad: {inventory[name]['quantity']}")
    else:
        time.sleep (0.2)
        print(WARNING + "Producto no encontrado en el inventario." + RESET)

#Update Products Prices
def update_products ():
    time.sleep (0.2)
    print(TITLE + "\n----------Actualizar Precios----------" + RESET)
    time.sleep (0.4)
    name = input("Ingrese nombre del producto: ")
    if name in inventory:
        try:
            new_price = float(input("Ingresa el nuevo precio: "))
            if new_price > 0:
                inventory[name]['price'] = new_price
                time.sleep (0.2)
                print(SUCCESS + "El precio se ha cambiado exitosamente." + RESET)
            else:
                time.sleep (0.2)
                print(DANGER + "El precio debe ser un numero positivo." + RESET)
        except ValueError:
            time.sleep (0.2)
            print(WARNING + "Por favor ingresa un numero valido." + RESET)
    else:
        time.sleep (0.2)
        print(WARNING + "Producto no encontrado en el inventario." + RESET)

#Delete Products From Inventory
def delete_products ():
    time.sleep (0.2)
    print(TITLE + "\n----------Eliminar Productos----------" + RESET)
    time.sleep (0.4)
    name = input("Ingrese el nombre del producto: ")
    if name in inventory:
        del inventory[name]
        time.sleep (0.3)
        print(SUCCESS + "Producto eliminado correctamente." + RESET)
    else:
        time.sleep (0.2)
        print(WARNING + "Producto no encontrado en el inventario." + RESET)

#Calculate The Total Value Of The Inventory
def calculate_total_value ():
    time.sleep (0.2)
    print(TITLE + "\n----------Calcular Valor Total----------" + RESET)
    time.sleep (0.2)
    total = 0
    for product in inventory.values():
        total += product['price'] * product['quantity']
    time.sleep (0.4)
    print(f"El valor total del inventario es: {total:.2f}")

#Function To Display All Products In The Inventory
def display_inventory ():
    time.sleep (0.2)
    print(TITLE + "\n----------Inventario Completo----------" + RESET)
    if not inventory:
        time.sleep (0.3)
        print(WARNING + "El inventario esta vacio." + RESET)
        return
    for name, details in inventory.items():
        time.sleep (0.2)
        print(f"- {name}: ${details['price']:.3f} | Cantidad: {details['quantity']}") 

#Function To Add Initial Products (at least 5 products)
def load_initial_products ():

    inventory["Laptop"] = {'price': 120.000, 'quantity': 5}
    inventory["Mouse"] = {'price': 25.500, 'quantity': 20}
    inventory["keyboard"] = {'price': 45.000, 'quantity': 10}
    inventory["Monitor"] = {'price': 300.000, 'quantity': 8}
    inventory["Cable USB"] = {'price': 8.900, 'quantity': 50}

#Function To Show The Main Menu
def show_menu ():
    time.sleep (0.9)
    print(TITLE + "========== Sistema De Gestion De Inventario ==========" + RESET)
    time.sleep (0.2)
    print("\n1.) Añadir Productos.")
    time.sleep (0.2)
    print("\n2.) Consultar Productos.")
    time.sleep (0.2)
    print("\n3.) Actualizar precios.")
    time.sleep (0.2)
    print("\n4.) Eliminar Productos.")
    time.sleep (0.2)
    print("\n5.) Calcular Valor Total Del Inventario.")
    time.sleep (0.2)
    print("\n6.) Mostrar Todos Los productos.")
    time.sleep (0.2)
    print("\n7.) Salir")

#Function To Run The Main Menu
def run_program ():
    load_initial_products()
    while True:
        show_menu()
        time.sleep (0.4)
        choice = input("\nElige una opcion (1 - 7): ")

        if choice == "1":
            time.sleep (0.5)
            add_products()
        elif choice == "2":
            time.sleep (0.5)
            check_products()
        elif choice == "3":
            time.sleep (0.5)
            update_products()
        elif choice == "4":
            time.sleep (0.5)
            delete_products()
        elif choice == "5":
            time.sleep (0.5)
            calculate_total_value()
        elif choice == "6":
            time.sleep (0.5)
            display_inventory()
        elif choice == "7":
            time.sleep (0.4)
            print (EXIT + "Saliendo del programa" + RESET)
            time.sleep (0.8)
            print (EXIT + "  ¡Hasta Pronto!" + RESET)
            break
        else:
            print(WARNING + "Opcion invalida" + RESET)

#Run The Program
run_program ()

