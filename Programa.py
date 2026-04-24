# tienes tu primer empleo necesitan realizar un programa en python, que entrege descuento a lo clientes y para ello comenzamos pidiendole al usuario su rut el cual debes
# validar los ochos digitos, en una casilla posterior validar el codigo de verificacion del rut posteriormente debes solicitar el nombre del cliente el monto de la compra para saber 
# si obtiene el descuento si o no toda compra menor a 10 mil pesos no obtiene descuento toda compra mayor a 11 mil pesos hasta 50 mil pesos obtiene un descuento 
# y toda compra mayor a 50 mil pesos obtiene un 20% de descuento.
# mi programa debe tener monto del descuento, total a pagar, y debera mostrar en pantalla tipo boleta el numero de indentificacion del usuario, nombre del usuario, monto de la compra,
# descuento aplicado y total final de la compra

while True:

    nombre = input("Ingrese su nombre: ")

    rut = input("Ingrese su rut(debe tener 8 digitos): ") 

    codigo_verificador = input("Ingrese el codigo verificador: ")

    monto = int(input("ingrese el monto de la compra: "))

    if rut == "21719254" and codigo_verificador == "-4":
 
        print("rut valido")


    elif nombre == "Benjamin":
    
        print("Bienvenido")
            

    if monto < 10000:
        
        print("Gracias por su compra")
        print(f"Su total es: {monto}")
        print(f"nombre del cliente: {nombre}")
        print(f"numero de indentificacion: {rut} {codigo_verificador}")
  
    elif monto >= 10000:

        print("se te agregara un 10%, de descuento")    
        print("Gracias por su compra")
        print(f"Su total es: {monto*1.1}")
        print(f"nombre del cliente: {nombre}")
        print(f"numero de indentificacion: {rut} {codigo_verificador}")
  
    elif monto > 50000:

        print("Se te agregara un 20%, de descuento")    
        print("Gracias por su compra")
        print(f"Su total es: {monto*1.2}")
        print(f"nombre del cliente: {nombre}")
        print(f"numero de indentificacion: {rut} {codigo_verificador}")

    else:

        print("Los datos no son validos")
  


    break


