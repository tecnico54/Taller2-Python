#Taller 1: Edad (mayor o menor)
print("==" * 30) 
#Peticiones al usuario
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
#Definir variable de texto como nulo
menor = ""
#Condiciones
if edad < 0:
    print("No se puede números negativos")
    exit()
elif edad > 18:
    print("Usted es mayor de edad")
elif edad < 18:
    falta = 18 - edad
#Mensaje
    menor = f"Usted es menor de edad, y le faltan {falta} años para cumplir 18 años"
#Mostrar resultado
print(f"Nombre: {nombre}\nEdad: {edad} años\n{menor}")
#Taller 2: Calificaciones
print("==" * 30)
#Peticiones al usuario
estudiante = input("Ingrese su nombre como estudiante: ")
calificacion = float(input("Ingrese su calificación (0.0 - 5.0): "))
#Definir variables de texto como nulo
nota = ""
desempeno = ""
#Condiciones
if calificacion < 0:
    print("No se puede números negativos")
    exit()
elif calificacion > 5:
    print("La calificación no puede ser mayor a 5.0")
else:
    nota = f"Estudiante: {estudiante}, su calificación es: {calificacion}"
    if calificacion < 3.0:
        desempeno = "Insuficiente"
    elif calificacion >= 3.0 and calificacion <= 3.4:
        desempeno = "Aceptable"
    elif calificacion >= 3.5 and calificacion <= 4.4:
        desempeno = "Bueno"
    elif calificacion >= 4.5 and calificacion <= 5.0:
        desempeno = "Excelente"
    if calificacion >= 3.0:
        print("\nNos complace informarle que usted aprobó la materia")
    else:
        print("\nLe informamos que usted reprobó la materia")
#Mostrar resultado
print(nota)
print(desempeno)
#Taller 3: Compras
print("==" * 30)
#Peticiones al usuario
peticion = input("¿Cuál es su nombre?: ")
valor = float(input("¿Cuál es el valor de su compra?: "))
#Definir variables numericas como nulo
descuento_porcentaje = 0
descuento = 0
#Definir
total = valor
#Condiciones
if valor < 0:
    print("No se puede números negativos")
    exit()
elif valor < 10000:
    print("Sin descuento")
elif valor > 10000 and valor < 299999:
    descuento_porcentaje = 0.10
    descuento = valor * descuento_porcentaje
    total = valor - descuento
elif valor > 300000 and valor < 499999:
    descuento_porcentaje = 0.15
    descuento = valor * descuento_porcentaje
    total = valor - descuento
else:
    valor >= 500000
    descuento_porcentaje = 0.20
    descuento = valor * descuento_porcentaje
    total = valor - descuento
#Mostrar resultado sin decimales y porsentaje
print(f"Valor: ${valor:,.0f}".replace(",","."))
print(f"Descuento: {descuento_porcentaje:.0%} de descuento")
print(f"Valor descontado: ${descuento:,.0f}".replace(",","."))
print(f"Total: ${total:,.0f}".replace(",","."))
#Taller 4: Temperatura
print("==" * 30)
#Peticiones al usuario
ciudad = input("Ingresar el nombre de la ciudad: ")
temparatura = int(input("Ingresar la temparatura actual en grados celsius: "))
#Definir variables de texto como nulo
clasificacion = ""
recomendacion = ""
#Condiciones
if temparatura <= 10:
    clasificacion = "Muy fria" 
    recomendacion ="Favor de llevar un abrigo grueso, bufanda y guantes"
elif temparatura <= 17:
    clasificacion = "Fria"
    recomendacion = "Favor de llevar una chaqueta o abrigo"
elif temparatura <= 25:
    clasificacion = "Templada"
    recomendacion = "Favor de llevar ropa ligera"
elif temparatura <= 32:
    clasificacion = "Caliente"
    recomendacion = "Favor de llevar ropa fresca y tomar agua"
else:
    temparatura > 32
    clasificacion = "Muy caliente"
    recomendacion = "Favor de llevar ropa muy fresca, hidratarse y evitar el sol"
#Mostrar resultado
print(f"Ciudad: {ciudad}")
print(f"Temperatura: {temparatura}°C")
print(f"Clasificación: {clasificacion}")
print(f"Recomendación: {recomendacion}")
#Taller 5:  Trabajo y sueldo
print("==" * 30)
#Peticiones al usuario
nombre = input("Ingrese el nombre del empleado: ")
horas = int(input("Ingrese las horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de cada hora: "))
#Definir variables numericas como nulo
horas_normales = 0
horas_extra = 0
pago_normal = 0
pago_extra = 0
salario_bruto = 0
descuento_porcentaje = 0
descuento = 0
salario_neto = 0
#Condicionales
if horas <= 0 or valor_hora <= 0:
    print("No se puede números negativos")
    exit()
elif horas <= 160:
    horas_normales = horas
    horas_extra = 0
else:
    horas_normales = 160
    horas_extra = horas - 160
    pago_normal = horas_normales * valor_hora
    pago_extra = horas_extra * valor_hora * 1.25
    salario_bruto = pago_normal + pago_extra
    descuento_porcentaje = 0.08
    descuento = salario_bruto * descuento_porcentaje
    salario_neto = salario_bruto - descuento
#Mostrar resultado
print(f"Empleado: {nombre}")
print(f"Horas normales: {horas_normales} horas")
print(f"Horas extra: {horas_extra} horas")
print(f"Pago hora normal: ${valor_hora:,.0f}".replace(",","."))
print(f"Pago hora extra: ${valor_hora * 1.25:,.0f}".replace(",","."))
print(f"Salario bruto: ${salario_bruto:,.0f}".replace(",","."))
print(f"Descuento: {descuento_porcentaje:.0%}")
print(f"Salario neto: ${salario_neto:,.0f}".replace(",","."))