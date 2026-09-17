#Taller 4:
print("==" * 30)
while True:
    try:
        def raiz_cuadrada(n):
            if n < 0:
                raise ValueError("No se permiten números negativos")
        raiz_cuadrada = n ** 0.5
        n = int(input("Ingrese un numero: "))
    except ValueError:
        print("Error: no se permiten caracteres")
        n = input("Ingresa un número valido")
        break
print(f"La raíz cuadrada de {n} es: {raiz_cuadrada}")