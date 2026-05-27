
Pikachu_Roll = 4500
Otaku_Roll = 5000
Pulpo_Venenoso_Roll = 5200
Anguila_Electrica_Roll = 4800


def menu ():

    Pikachu = 0
    Otaku = 0
    Pulpo = 0
    Anguila = 0

    
    while True:
        
        print("============Menu==========")
        print("\n1. Pikachu_roll")
        print("2. Otaku Roll")
        print("3. Pulpo Venenos Roll")
        print("4. Anguila Electrica Roll")
        print("5. Salir\n")

        

        opc = input("Seleccione: ")

        if opc == "1":
                Pikachu +=  1

        elif opc == "2":
                Otaku += 1

        elif opc == "3":
                Pulpo += 1

        elif opc == "4":
                Anguila += 1
                
        elif opc == "5":
                break


        else:
             print("Ingrese una opcion valida")

        

    return Pikachu, Otaku, Pulpo, Anguila



def Descuento(subtotal):

    while True:
        codigo = input("Ingrese el codigo de descuento (x para salir): ")

        if codigo == "soyotaku":
            return subtotal * 0.10
        
        elif codigo == "x":
            return 0
    
        else:
            print("Codigo no valido")


Pikachu, Otaku, Pulpo, Anguila = menu()

subtotal = (
    Pikachu_Roll * Pikachu +
    Otaku * Otaku_Roll +
    Pulpo * Pulpo_Venenoso_Roll +
    Anguila * Anguila_Electrica_Roll 
)
descuento_total = Descuento(subtotal)
total = subtotal - descuento_total

print(f"Pikachu Roll: {Pikachu}")
print(f"Otaku Roll: {Otaku}")
print(f"Pulpo Venenoso Roll: {Pulpo}")
print(f"Anguila Electrica Roll: {Anguila}")


print(f"\nSubtotal: {subtotal}")
print(f"Descuento: {int(descuento_total)}")
print(f"Total: {int(total)}")
