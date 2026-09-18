#Taller 1:
print("==" * 30)
try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    operador = input("Ingrese el operador (+, -, *, /): ")
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        resultado = num1 / num2
    else:
        print("Operador no válido.")
        resultado = None
    if resultado is not None:
        print(f"Resultado: {resultado:.0f}")
except ValueError:
    print("Error: debe ingresar números válidos.")
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero.")
#Taller 2:
print("==" * 30)
archivo = ""
try:
    nombre = input("Ingrese el nombre del archivo: ")
    archivo = open(nombre, "r")
    print("El archivo se abrió correctamente.")
except FileNotFoundError:
    print("Error: el archivo no existe.")
print(archivo)
#Taller 3:
print("==" * 30)
dia = ""
mes =""
ano = ""
try:
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    ano = int(input("Año: "))
    print(f"La fecha: {dia}/{mes}/{ano}")
except ValueError:
    print("Error: no se permite carateres")
#Taller 4:
print("==" * 30)
def raiz_cuadrada(n):
    if n < 0:
        raise ValueError
    return n ** 0.5
while True:
    try:
        n = int(input("Ingrese un número: "))
        if n < 0:
            print("No se permiten números negativos")
            continue
        raiz = raiz_cuadrada(n)
        print(f"La raíz cuadrada de {n} es: {raiz:.0f}")
        break
    except ValueError:
        print("El número es inválido")
#Taller 5:
print("==" * 30)
#Descripción
print("El Programa te va a solitar números infinitamente, si quisieras parar solo tienes que" \
        " escribir fin\n")
#Arreglo
numeros = []
#Definición
suma = 0
cantidad = 0
promedio = 0
while True:
    try:
        #Bucle
        digitalizacion = float(input("Ingresar números: "))
        #Añadir al arreglo
        numeros.append(digitalizacion)
        #¿Cuantos hay?
        cantidad = len(numeros)
        #Sumar y promediar
        promedio = sum(numeros) / cantidad 
        digitalizacion == "fin"
    except ValueError:
        print(f"El programa se detuvo\nCantidad: {cantidad}\nPromedio: {promedio:,.1f}".replace(",","."))
        exit()