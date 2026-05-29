suites = 0
estandar = 0 

while True:
    try:
        cantidad = int(input("Ingrese la cantidad de habitaciones a registrar: "))

        if cantidad > 0:
            break
        else:
            print("Cantidad invalida! Ingresa un entero positivo para continuar.")

    except:
        print("Cantidad invalida! Ingresa un entero positivo para continuar.")

for i in range(cantidad):
    print(f"\nRegistro de habitaciones {i + 1}")

    while True:
        numero = input("Ingrese el numero de habitacion: ")

        if len(numero) >= 6 and " " not in numero:
            break
        else:
            print("¡Numero de habitaciones invalido! Debe tener al menos 6 caracteres y no contener espacios")

    while True:
        try:
            tarifa = int(input("Ingrese tarifa nocturna: "))

            if tarifa > 0:
                break
            else:
                print("¡Error tarifario! Ingresa un numero entero positivo para la tarifa nocturna")

        except:
            print("¡Error tarifario! Ingresa un numero entero positivo para la tarifa nocturna")

    if tarifa > 90000:
        suites += 1
    else:
        estandar += 1

print(f"\n¡El hotel cuenta con {suites} Suites Ejecutivas y {estandar} Habitaciones estandar! ¡Check-in disponible!")            
