espacios_disponibles = 60
espacios_ocupados = 0

print("¡Bienvenido al sistema de gestion de espacios del Almacen Industrial!")

while True:

    print("=====MENU PRINCIPAL=====")
    print("\n1. Espacios disponibles")
    print("2. Ocupar espacio")
    print("3. Liberar espacio")
    print("4. Espacios actualmente ocupados")
    print("5. Salir\n")

    opc = input("Ingrese la opcion que desea: ")

    if opc == "1":
        print(f"Espacios disponibles actualmente: {espacios_disponibles}")

    elif opc == "2":
        while True:
            try:
                cantidad = int(input("Ingrese cantidad de espacios a ocupar: "))

                if cantidad <= 0:
                    print("¡Cantidad invalida!. Ingresa un numero entero mayor a 0")
                
                elif cantidad > espacios_disponibles:
                    print("No hay suficientes espacios disponibles para realizar la ocupacion.")

                else:
                    espacios_disponibles -= cantidad
                    espacios_ocupados += cantidad

                    print("Ocupacion realizada correctamente")
                    break
            except:
                print("¡Cantidad invalida!. Ingresa un numero entero mayor a 0")

    elif opc == "3":
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de espacios que desea liberar: "))

                if cantidad <= 0:
                    print("¡Cantidad invalida! ingresa un numero entero mayor a 0")

                elif cantidad > espacios_ocupados:
                    print("No puedes liberar mas espacios de los que estan ocupados actualmente")
                    break

                elif espacios_disponibles + cantidad > 60:
                    print("No se puede superar la cantidad maxima de 60 espacios")
                    break

                else:
                    espacios_disponibles += cantidad
                    espacios_ocupados -= cantidad

                    print("Liberacion realizada correctamente")
                    break

            except:
                print("Cantidad invalida debe ingresar un numero entero mayor a 0")

    elif opc == "4":
        print(f"Espacios actualmente ocupados: {espacios_ocupados}")

    elif opc == "5":
        print("Gracias por utilizar nuestro software, hasta la proxima")
        break

    else:
        print("Opcion invalida. Selecciona un opcion entre 1 y 5")                            