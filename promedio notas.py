# Solicitar el nombre
nombre = input("Por favor, dime tu nombre: ")

# Listas
notas = []
for i in range(4):
    nota = float(input(f"Ingresa la nota numero {i + 1}: "))
    notas.append(nota)

suma = 0

for nota in notas:
    suma = suma + nota

promedio = suma / len(notas)

estudiante = {
    "nombre" : nombre,
    "notas" : notas,
    "promedio" : promedio 
}

# Mostrar

print("\nResumen")
print("______________________________________")
print("Nombre:", estudiante["nombre"])
print("Nota: ", estudiante["notas"])
print("Promedio: ", estudiante["promedio"])