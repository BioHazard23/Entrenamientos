                                            #Programa de gestion de calificaciones
                                                #por: Juan Manuel Arango Arana

#Determina si una nota aprueba o reprueba
calificacion =  int(input("Ingresa una nota (0 - 100): "))

if calificacion < 0 or calificacion > 100:
    print("La nota ingresada no es valida")
elif calificacion >= 60:
    print("Aprobaste")
else:
    print("Reprobaste")

#Es para ingresar una lista de calificaciones
entrada = input("Ingresa una lista de calificaciones separadaspor comas (0 - 100): ")
lista = entrada.split(",")
calificaciones = []

for cal in lista:
    cal = cal.strip()
    if cal.isdigit():
        valor = int(cal)
        if 0 <= valor <= 100:
            calificaciones.append(valor)
        else:
            print(f"Valor fuera del rango: {valor}")
    else:
        print(f"Valor no valido: {cal}")

#Aqui se calcula el promedio de las notas
suma = 0

for cal in calificaciones:
    suma += cal

if len(calificaciones) > 0:
    promedio = suma / len(calificaciones)
    print(f"\nEl promedio de las calificaciones es: {promedio:.2f}")
else:
    print("\nNo se ingresaron calificaciones validas para calcular el promedio")

#Se cuenta cuantas calificaciones son mayores a un valor dado
valor_comp = int(input("\nIngresa un valor para comparar: "))
i = 0
contador_mayores = 0

while i < len(calificaciones):
    if calificacion[i] > valor_comp:
        contador_mayores += 1
    i + 1

print(f"Hay {contador_mayores} calificaciones mayores que {valor_comp}")

#Se verifica y se cuenta una calificacion que el usuario ingreso
valor_especifico = int(input("\nIngresa una calificacion especifica para buscar: "))
encontrado = False
contador = 0

for cal in calificaciones:
    if cal < 0 or cal > 100:
        continue
    if cal == valor_especifico:
        contador += 1
        encontrado = True
    if contador > 10: #Esto es para que no se repita muchas veces
        print("demasiadas repeticiones, la busqueda se detiene")
        break

if encontrado:
    print(f"La calificacion {valor_especifico} aparece {contador} veces")
else:
    print(f"La calificacion {valor_especifico} no se encuentra en la lista ")