def mostrar_menu():
    print()
    print("___________________________Menu Principal_________________________")
    print("1. Agregar vehiculo")
    print("2. Buscar vehiculo")
    print("3. Eliminar vehiculo")
    print("4. Actualizar vehiculo")
    print("5. Mostrar vehiculo")
    print("6. Salir")
    print("__________________________________________________________________")


    # Funcion para leer

    def leer_opcion():
        try:
            opcion = int(input("Selecciona una opcion: "))

            if opcion >= 1 and opcion <= 6:
                return opcion

            else:
                print("Error, Debe ingresar una opcion del 1 al 6")
                return 0 

        except ValueError:
            print("Ingresa un numero entero")
            return 0
        
def validacion_modelo(modelo):
    if modelo.strip() != "":
        return True       

    else:
        return False
        
# Funcion de año

def validar_anio(anio):
    if anio > 1980:
        return True
    else:
        return False
    
# Funcion de precio
  
def validar_precio(precio):
    if precio > 0:
        return True
    else:
        return False    
    
# Funcion de vehiculo

def agregar_vehiculo(lista_vehiculos):
    print()
    print("Agregar Vehiculo") 

    modelo = input("Agrega el modelo del vehiculo: ")
    
    if not validacion_modelo(modelo):
        print("Error, blabla")
        return
    
    try:
        anio = int(input("Ingrese el año del vehiculo: "))

        if not validar_anio(anio):
            print("Error, blabla")
            return
        
    except ValueError:
        print("Error: Debe ingresar un año entero")

    try:
        precio = float(input("Ingrese el precio del vehiculo: "))

        if not validar_precio(precio):
            print("Error, el precio debe ser mayor que cero")
            return

    except ValueError:
        print("Error, el precio debe ser un numero decimal")
        return



    vehiculo = {
        "modelo": modelo.strip(),
        "anio": anio,
        "precio": precio,
        "disponible": False 

    }            

    lista_vehiculos.append(vehiculo)
    
    print("Vehiculo agregado correctamente")
