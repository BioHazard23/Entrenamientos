
                                            #Programa de gestion de calificaciones
                                                #por: Juan Manuel Arango Arana

#Determina si una nota aprueba o reprueba
nota =  int(input("Ingresa una nota (0 - 100): "))

if nota < 0 or nota > 100:
    print("La nota ingresada no es valida")
elif nota >= 60:
    print("Aprobaste")
else:
    print("Reprobaste")

#Es para ingresar una lista de calificaciones
entrada = input("\nIngresa varias calificaciones separadas por comas: ")
lista_texto = entrada.split(",")
calificaciones = []

for cal in lista_texto:
    cal = cal.strip()
    if cal.isdigit():
        cal_int = int(cal)
        if 0 <= cal_int <= 100:
            calificaciones.append(cal_int)
        else:
            print(f"Valor fuera del rango: {cal_int}")
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
valor = int(input("\nIngresa un valor para comparar: "))
i = 0
mayores = 0

while i < len(calificaciones):
    if calificaciones[i] > valor:
        mayores += 1
    i += 1

print(f"{mayores} calificaciones son mayores que {valor}")

#Se verifica y se cuenta una calificacion que el usuario ingreso
buscar = int(input("\nIngresa una calificacion especifica para buscar: "))
encontrado = False
contador = 0

for cal in calificaciones:
    if cal == buscar:
        contador += 1
        encontrado = True
    else:
        continue

if encontrado:
    print(f"La calificacion {buscar} aparece {contador} veces")
else:
    print(f"La calificacion {buscar} no se encuentra en la lista ")
