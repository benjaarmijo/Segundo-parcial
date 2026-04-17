intento = 5

while intento > 0:

    usuario = input("Ingrese su usuario: ")
    password = input("ingrese su contraseña: ")

    if usuario == "Benjamin" and password == "Benja123":
            print("Datos ingresados correctos")
            print("="*50)
            print(f"Bienvenido, {usuario}")
            print("="*50)
            break
    
    else:
        
        intento -= 1

        print(f"Datos incorrecto, te quedan, {intento}")
        if intento == 0:
            print("Acceso denegado")


