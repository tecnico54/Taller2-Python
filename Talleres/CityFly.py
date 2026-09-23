#Opciones
print("1.Medellìn -> Bogotà")
print("2.Medellìn -> Cali")
print("3.Medellìn -> Barranquilla")
print("4.Medellìn -> Cartagena\n")
print("--------Menù-----------")
print("1 | 2 | 3 | 4\n")
#Definiciones
cantidad = 0
total = 0
menu = ""
destino = ""
cantidad_pasajeros = ""
arreglo = ""
while True:
    try:
        menu = int(input("Seleccione una opción: "))
        if menu < 0 and menu > 4:
            print("Error: seleccione una opción entre 1 y 4")
    except ValueError:
        print("Error: debe ingresar un número")
        continue
    while menu != 4:
        #Opción 1
        if menu == 1:
            destino = "Medellìn -> Bogotá"
            print(f"Usted seleccionó la opción {menu}, su destino es: {destino}")
            compra = 120000
            while True:
                try:
                    cantidad = int(input("¿Cuantos tiquetes?: "))
                    if cantidad < 0:
                        print("Error: no se permite números negativos")
                except ValueError:
                    print("Error: Ingrese un número")
                total = cantidad * compra
                arreglo = []
                for p in range(cantidad):
                    while True:
                        if cantidad == 1:
                            cantidad_pasajeros = input("Ingrese el pasajero: ")
                            if cantidad_pasajeros.isalpha():
                                break
                            else:
                                print("Error: Solo caracteres")
                    print(f"\nPasajero: {cantidad_pasajeros}")
                else:
                    for p in range(1, cantidad + 1):
                        while True:
                            cantidad_pasajeros = input(f"Ingrese los pasajeros {p}: ")
                            if cantidad_pasajeros.isalpha():
                                break
                            else:
                                print("Error: Solo caracteres")
                        arreglo.append(cantidad_pasajeros)
                    print(f"\nPasajeros: {", ".join(arreglo)}")
                    break
            break
        #Opción 2
        elif menu == 2:
            destino = "Medellìn -> Cali"
            print(f"Usted seleccionó la opción {menu}, su destino es: {destino}")
            compra = 100000
            while True:
                try:
                    cantidad = int(input("¿Cuantos tiquetes?: "))
                    if cantidad < 0:
                        print("Error: no se permite números negativos")
                except ValueError:
                    print("Error: Ingrese un número")
                total = cantidad * compra
                arreglo = []
                for p in range(cantidad):
                    while True:
                        if cantidad == 1:
                            cantidad_pasajeros = input("Ingrese el pasajero: ")
                        if cantidad_pasajeros.isalpha():
                            break
                        else:
                            print("Error: Solo caracteres")
                    print(f"\nPasajero: {cantidad_pasajeros}")
                else:
                    for p in range(1, cantidad + 1):
                        while True:
                            cantidad_pasajeros = input(f"Ingrese los pasajeros {p}: ")
                            if cantidad_pasajeros.isalpha():
                                break
                            else:
                                print("Error: Solo caracteres")
                        arreglo.append(cantidad_pasajeros)
                    print(f"\nPasajeros: {", ".join(arreglo)}")
                    break
            break
        #Opción 3
        elif menu == 3:
            destino = "Medellìn -> Barranquilla"
            print(f"Usted seleccionó la opción {menu}, su destino es: {destino}")
            compra = 150000
            while True:
                try:
                    cantidad = int(input("¿Cuantos tiquetes?: "))
                    if cantidad < 0:
                        print("Error: no se permite números negativos")
                except ValueError:
                    print("Error: Ingrese un número")
                total = cantidad * compra
                arreglo = []
                for p in range(cantidad):
                    while True:
                        if cantidad == 1:
                            cantidad_pasajeros = input("Ingrese el pasajero: ")
                            if cantidad_pasajeros.isalpha():
                                break
                            else:
                                print("Error: Solo caracteres")
                    print(f"\nPasajero: {cantidad_pasajeros}")
                else:
                    for p in range(1, cantidad + 1):
                        while True:
                            cantidad_pasajeros = input(f"Ingrese los pasajeros {p}: ")
                            if cantidad_pasajeros.isalpha():
                                break
                            else:
                                print("Error: Solo caracteres")
                        arreglo.append(cantidad_pasajeros)
                    print(f"\nPasajeros: {", ".join(arreglo)}")
                    break
            break
        #Opción 4
        elif menu == 4:
            destino = "Medellìn -> Cartegena"
            print(f"Usted seleccionó la opción {menu}, su destino es: {destino}")
            compra = 200000
            while True:
                try:
                    cantidad = int(input("¿Cuantos tiquetes?: "))
                    if cantidad < 0:
                        print("Error: no se permite números negativos")
                except ValueError:
                    print("Error: Ingrese un número")
                total = cantidad * compra
                arreglo = []
                for p in range(cantidad):
                    while True:
                        if cantidad == 1:
                            cantidad_pasajeros = input("Ingrese el pasajero: ")
                        if cantidad_pasajeros.isalpha():
                            break
                        else:
                            print("Error: Solo caracteres")
                    print(f"\nPasajero: {cantidad_pasajeros}")
                else:
                    for p in range(1, cantidad + 1):
                        while True:
                            cantidad_pasajeros = input(f"Ingrese los pasajeros {p}: ")
                            if cantidad_pasajeros.isalpha():
                                break
                            else:
                                print("Error: Solo caracteres")
                        arreglo.append(cantidad_pasajeros)
                    print(f"\nPasajeros: {", ".join(arreglo)}")
                    break
            break
    print(f"Destino: {destino}\nTotal a pagar: {total:,.0f}".replace(",","."))