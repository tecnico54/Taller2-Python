#Taller 1: Base por altura
print("=="*30)
#Peticiones al usuario
base = float(input("Ingrese el ancho de la estructura: "))
altura = float(input("Ingrese el largo de la estructura: "))
#Cálcular
estuctura = base * altura
#Mostrar resultado
print("La Estructura es de:", estuctura, "m²")
#Taller 2: Promedio
print("=="*30)
#Peticiones al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
#Cálcular
promedio = (num1 + num2 + num3) / 3
#Mostrar resultado
print(f"El promedio es: {promedio:,.0f}".replace(",","."))
#Taller 3: Datos (nombre y edad)
print("=="*30)
#Peticiones al usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
#Mostrar resultado
print(f"Hola, mi nobre es {nombre} y tengo {edad} años")
#Taller 4: Convergencia (pesos a dollares)
print("=="*30)
#Petición al usuario
pesos = float(input("Ingrese el valor en pesos colombianos: "))
#Cálcular
dolares = pesos / 4000
#Mostrar resultado
print(f"${pesos} COP equivalen a ${dolares} USD")
#Taller 5: Segundos a minutos/horas
print("=="*30)
#Petición al usuario
segundos = int(input("Ingrese la cantidad de segundos: "))
#Cálcular
minutos = segundos / 60
horas = segundos / 3600
#Mostrar resultado
print(f"{segundos} segundos equivalen a {minutos} minutos")
print(f"{segundos} segundos equivalen a {horas} horas")