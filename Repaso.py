#Ciclo Infinito para que se repita todo el proceso
lista_pasajeros = []
while True:
    print("=== TIQUETE DE BUS === \n")
    try:
        menu = int(input("""
        Seleccion Ruta a comprar:
        1. Medellín - Bogotá
        2. Medellín - Cali
        3. Medellín -Barranquilla
        4. Medellín Cartagena
        5. Salir  """))
        if menu in range(1,4):
            valor_tiquete= 0 
            if menu == 1:
                valor_tiquete = 120000
            elif menu == 2:
                valor_tiquete = 100000
            elif menu == 3:
                valor_tiquete = 150000
            elif menu == 4:
                valor_tiquete = 200000
            try:
                cantidad = int(input("Cantidad de tiquetes a comprar : "))
                for i in range(cantidad):
                    pasajero=input(f"Ingrese el nombre del pasajero {i+1} ")
                    #Guardar el valor de la variable en la lista
                    lista_pasajeros.append(pasajero)
                #Mostrar Todo
                print(f"""
                === RESUMEN COMPRA ===
                -Cantidad Pasajeros = {cantidad}
                -Valor Tiquet = {valor_tiquete}
                -Total : {cantidad * valor_tiquete}
                -Pasajeros = {lista_pasajeros}      
                """)
            except ValueError:
                print("Ingrese una cantidad Valida")

        elif menu == 5:
            print("Saliendo del Sistema")
            break
        else:
            print("Opcion Invalida")
            break
    except ValueError:
        print("Ingrese una opcion Valida.")