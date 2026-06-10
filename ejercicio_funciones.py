# desarrolle un programa en python que solicite un lista de numeros enteros, separados por espacios, valide que los numeros sean enteros, separe los numeros pares de los impares, 
# muestra ambas listas y utilize por lo menos una funcion

def separar_pares_impares(lista_numero):
    pares = []
    impares = []

    for numero in lista_numero:
        if numero % 2 == 0:
            pares.append(numero)

        else:
            impares.append(numero)
            
    return pares, impares            

entrada = input("Ingrese una lista de numeros enteros separados entre si: ")

try:
    numeros = [int(x) for x in entrada.split()]

    pares, impares = separar_pares_impares(numeros)

    print("\nLista de numeros pares: ")
    print(pares)

    print("\nLista de numeros impares: ")
    print(impares)

except ValueError:
    print("Error: Debe ingresar unicamente numeros enteros separados por espacios")


