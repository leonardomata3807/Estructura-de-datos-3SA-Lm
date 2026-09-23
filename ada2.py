import random

alumnos = 100000
materias = 70


matriz = []

for i in range(alumnos):
    fila = []

    for j in range(materias):
        fila.append(random.randint(1, 10))

    matriz.append(fila)


print("\n          ", end="")

for j in range(materias):
    print("Materia", j + 1, end="    ")

print()

for i in range(alumnos):
    print("Alumno", i + 1, end=":    ")

    for j in range(materias):
        print(matriz[i][j], end="          ")

    print()


print("\nBuscar calificacion y alumno")

alumno = int(input("Escribe el numero del alumno: "))
materia = int(input("Escribe el numero de la materia: "))


if alumno >= 1 and alumno <= alumnos and materia >= 1 and materia <= materias:

    calificacion = matriz[alumno - 1][materia - 1]

    print("\nAlumno:", alumno)
    print("Materia:", materia)
    print("Calificacion:", calificacion)

else:
    print("\nEl alumno o la materia no existen.")
