moto = 15000
candado = 9000

while True:
    try:
        dias = int(input("Ingrese la cantidad de dias: "))
        break
    except:
        print("Ingrese un numero valido")


estudiante = input("Es estudiante(si/no): ").lower()

descuento_moto = 0

if dias >= 20:
    
    if estudiante == "si":
        descuento_moto = 0.25

    else:
        descuento_moto = 0.15

elif dias >= 10:
    if estudiante == "si":
        descuento_moto = 0.15

    else:
        descuento_moto = 0.08

else:
    descuento_moto = 0

total_moto = moto *(1 - descuento_moto)    


descuento_candado = 0

if candado < 10:
    descuento_candado = 0

elif candado < 15:
    descuento_candado = 0.15

else:
    descuento_candado = 0
    if estudiante == "si":
        descuento_candado += 0.12

total_candado = candado *(1 - descuento_candado)


print(50*"-")
print(f"Total moto, {total_moto}")
print(f"Total candado, {total_candado}")
print(50*"-")

    