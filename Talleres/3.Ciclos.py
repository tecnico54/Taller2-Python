#Taller 1: Adivina el numero
print("==" * 30)
#Libreria para los numeros aleatorios
import random
#Intrucción
print("El sistema va a mostrarle aleatoriamente números enteros,\nusted debera adivinarlos.")
#Petición de selección
print("Seleccionar un números: ")
#Ciclo For (Para mostrar los números de 1 al 10)
for i in range(1, 11): 
    print(i, end=" ")
#Peticiones al usuario
numero = int(input("\nIngrese un número: "))
#Números aleatorios (enteros)
numero_aleatorio = 3
#Ciclo while (Mientras)
while numero != numero_aleatorio:
#Condiciones (si es menor o igual a 0 o si es mayor a 10)
    if numero <= 0:
        print("Error")
        numero = int(input("\nIngrese nuvamente un número positivo: "))
    elif numero > 10:
        print("Error")
        numero = int(input("\nIngrese nuvamente un número menor a 10: "))
    else:
        print("Lo siento, intantarlo otra vez")
        numero = int(input("\nIntetarlo nuvamente: "))
else:
    print("¡Felicidades, adivinaste el número!")
#Mostrar resultado
print(f"El número aleatorio es: {numero_aleatorio}")
#Taller 2: Cuenta regresiva
print("==" * 30)
#Petición al usuario
numero_positivo = int(input("Ingrese un número: "))
#Condiciones (si es menor a 0)
if numero_positivo < 0:
    print("Error")
    exit()
#Ciclo while (Mientras)
while numero_positivo >= 0:
        print(numero_positivo, end=" ")
        numero_positivo = numero_positivo -1
#Mostrar resultado
print("La operación ha finalizo")
#Taller 3: Números impares
print("==" * 30)
print("Los números enteros son:")
#Ciclo For (Para mostrar los números de 1 al 100)
for e in range(1, 101):
    print(e, end=" ")
print("Los números impares son:")
#Ciclo For (Para mostrar los números de 1 al 100 (impares))
for i in range(1, 101):
    if i % 2 != 0:
        print(i, end=" ")
#Taller 4: Menú
print("==" * 30)
#libreria de la fecha actual
from datetime import date
#Definir la variable como nula
opcion = 0
#Mostrar fecha actual
fecha = date.today()
#Menú
print("\nOpción 1 | Opción 2 | Opción 3")
#Ciclo while (Mientras)
while opcion != 3:
#Petición
    opcion = int(input("\nSeleccionar una opción: "))
#Condiciones
    if opcion == 1:
        print("Bienvenido/a")
    elif opcion == 2:
        print(f"La fecha actual es: {fecha.strftime("%A %d/%m/%y")}") 
    elif opcion == 3:
        print("Saliendo...")
        break
    else:
        print("La opción no coincide")
        exit()
#Taller 5: Registro de notas y promedio
print("==" * 30)
#Petición al usuario
nota = int(input("¿Cuantas notas desea registrar?: "))
#Definir la variable como nula
cantidad = 0
suma = 0
promedio = 0
#Condición (aumento de notas)
if nota <= 0:
    print("Error, no puede ser numeros negativos o que sea 0")
    exit()
#Ciclo For (Para Aumento de notas segun el usuario)
for n in range(1, nota + 1):
    cantidad = float(input(f"Digite la nota {n}: "))
#Cálcular
    suma = suma + cantidad
    promedio = suma / nota
#Condiciones (Notas)
    if nota <= 0:
        print("Error, la nota no puede ser numeros negativos o que sea 0")
        exit()
print(f"El promedio es: {promedio}")
if promedio >= 3.0:
    print("El estudiante aprobó")
else:
    print("El estudiante reprobó")