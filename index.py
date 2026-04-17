intento = 3

while intento > 0:
    
    password = input("Ingrese su clave: ")
    if password == "1234":
        print("Bienvenido")
        break
    else:

        intento -= 1

        print(f"Intento fallido, te falta, {intento}")

        if intento == 0:
            print("Acceso denegado")
        