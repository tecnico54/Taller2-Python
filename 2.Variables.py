# Ejercicio 1: Suma de dos números
print("Ejercicio 1: suma de dos números")
print("=="*30) 
numero1=float(input("Ingrese el primer número: "))
numero2=float(input("Ingrese el sugundo número: "))
suma = numero1 + numero2
print(f"La suma es: {suma}\n")
# Ejercicio 2: Área de un rectángulo
print("Ejercicio 2: Área del rectángulo")
print("=="*30) 
base    = float(input("Ingrese la base del rectángulo: "))
altura  = float(input("Ingresar la altura del rectángulo: "))
area    = base * altura
print("El área del rectángulo es: ", area, "\n")
# Ejercicio 3: Conversión de minutos a horas y minutos
print("Ejercicio 3: Calcula la cantidad total")
print("=="*30) 
minutos_totales = int(input("Ingrese la cantidad de minutos: "))
horas   =minutos_totales // 60
minutos =minutos_totales % 60
print(minutos_totales, "minutos equivalen a", horas, "horas y", minutos, "minutos \n")
# Ejercicio 4: Cálculo del precio con descuento
print("Ejercicio 4: Calcula la cantidad del precio con descuento")
print("=="*30) 
precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
valor_descuento = precio * (descuento / 100)
precio_final = precio - valor_descuento
print("El precio final a pagar es: ", precio_final, "\n")
# Ejercicio 5: Intercambio de valores entre dos variables
print("Ejercicio 5: Intercambio de valores entre dos variables")
print("=="*30)
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
auxiliar = a   # guardar temporalmente el valor de a
a = b          # a toma el valor de b
b = auxiliar   # b toma el valor original de a
print("Después del intercambio: a =", a, ", b =", b)