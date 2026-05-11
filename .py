suma = 0

for i in range (5):
    
    while True:
        try:
            numero = float(input(f"Ingrese el numero {i + 1}: "))
            
            suma = suma + numero

            break
        except:

            print("Error, debe ingresar un numero valido")

print("La suma total es: ", suma)            

"""
Hay un pequeña tienda que desea modernizar su sistema de venta, actualmente el vendedor lleva un modesto registro manual y al final del dia debe calcular todo lo vendido. 
Para facilitar el trabajo necesitamos crear un programa en python y cuando hagamos la venta le debe solicitar sus datos, nombre, rut, el carnet en general, una vez que tenga todos
los datos el usuario debe introducir 10 productos para comprar, una vez realizada la compra, debe mostrar el resultado de la compra si tiene alguna descuento muestra el descuento
"""