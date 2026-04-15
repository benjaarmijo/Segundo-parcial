##Duoc a contratado sus servicios para realizar un login en python, debe validar el usuario y la clave

while  True:
    print("=======BIENVENIDO A DUOC=======")
    usuario = input("Ingrese su usuario: ")

    if usuario == "Duoc.cl":
        print("Usuario correcto")
    else:
        print("Usuario incorrecto")
        break

    clave = input("Ingrese la clave: ")

    if clave == "Duoc2026":
        print("Clave correcta, bienvenido")
    else:
        print("Clave incorrecta")
            