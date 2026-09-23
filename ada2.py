import random

alumnos = 1000000
materias = 70

matriz = []

for i in range(alumnos):
    fila = []

    for j in range(materias):
        fila.append(random.randint(1, 10))

    matriz.append(fila)


print("\n      ", end="")

for j in range(materias):
    print("Materia", j + 1, end="   ")

print()

for i in range(alumnos):
    print("Alumno", i + 1, end=": ")

    for j in range(materias):
        print(matriz[i][j], end="        ")

    print()


numero = int(input("\n¿Qué alumno quieres consultar?: "))

if numero >= 1 and numero <= alumnos:

    print("\nDatos del Alumno", numero)

    for j in range(materias):
        print("Materia", j + 1, ":", matriz[numero - 1][j])

else:
    print("Ese alumno no existe.")