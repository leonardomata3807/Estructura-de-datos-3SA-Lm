def busqueda_binaria(lista, objetivo):

    inicio = 0
    fin = len(lista) - 1
    comparaciones = 0

    while inicio <= fin:
        medio = (inicio + fin) // 2
        comparaciones += 1
        if lista[medio]["matricula"] == objetivo:
            return medio, comparaciones
        elif objetivo < lista[medio]["matricula"]:
            fin = medio - 1        
        else:
            inicio = medio + 1     
    return -1, comparaciones


def main():
    alumnos = [
        {"matricula": 1001, "nombre": "Ana López", "promedio": 92},
        {"matricula": 1005, "nombre": "Luis Pérez", "promedio": 85},
        {"matricula": 1008, "nombre": "María Gómez", "promedio": 97},
        {"matricula": 1012, "nombre": "Carlos Ruiz", "promedio": 78},
        {"matricula": 1015, "nombre": "Sofía Martín", "promedio": 88},
        {"matricula": 1020, "nombre": "Jorge Díaz", "promedio": 81},
        {"matricula": 1024, "nombre": "Elena Castro", "promedio": 94},
        {"matricula": 1030, "nombre": "Pedro Salas", "promedio": 73},
        {"matricula": 1033, "nombre": "Laura Vega", "promedio": 90},
        {"matricula": 1040, "nombre": "Diego Torres", "promedio": 86},
    ]
    
    alumnos.sort(key=lambda a: a["matricula"])

    print("=== BÚSQUEDA BINARIA: REGISTRO DE ALUMNOS ===")
    print("Matrículas:", ", ".join(str(a["matricula"]) for a in alumnos))

    try:
        matricula = int(input("\nMatrícula a buscar: "))
    except ValueError:
        print("Debes escribir un número entero.")
        return

    pos, comp = busqueda_binaria(alumnos, matricula)

    if pos != -1:
        a = alumnos[pos]
        print(f"\n✔ Encontrado en la posición {pos}")
        print(f"  Alumno: {a['nombre']} | Promedio: {a['promedio']}")
    else:
        print("\n✘ La matrícula no está registrada.")
    print(f"  Comparaciones realizadas: {comp}")


if __name__ == "__main__":
    main()