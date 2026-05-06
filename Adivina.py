from random import randint
while True:
    try:

        num1 = int(input("Ingrese un numero menor: "))
        num2 = int(input("Ingrese un numero mayor: "))
        break
    
    except:
        print("Ingrese un numero valido")

if num1 >= num2:
    print("Error, el primer numero debe ser menor")

else:
    
    numero = randint(num1, num2)


if numero < num1 or numero > num2:
    numero = numero //  num1


for i in range(3):
    intento = int(input("advina el numero: "))

    if intento == numero:
        print("Ganaste")
        break
    
    else:
        print("Incorrecto")

else:
    print(f"Perdiste, el numero era: {numero}") 
