def intercalar(lista_a, lista_b, clave=lambda x: x):
    
    resultado = []
    i = j = 0

   
    while i < len(lista_a) and j < len(lista_b):
        if clave(lista_a[i]) <= clave(lista_b[j]):
            resultado.append(lista_a[i])
            i += 1
        else:
            resultado.append(lista_b[j])
            j += 1

   
    resultado.extend(lista_a[i:])
    resultado.extend(lista_b[j:])
    return resultado


def mostrar(titulo, alumnos):
    print(f"\n{titulo}")
    print("-" * 40)
    for nombre, promedio in alumnos:
        print(f"{nombre:<12} {promedio:>5.1f}")


if __name__ == "__main__":
    
    grupo_a = [("Ana", 6.5), ("Luis", 7.8), ("Marta", 8.9), ("Pedro", 9.5)]
    grupo_b = [("Sofía", 7.0), ("Carlos", 8.2), ("Elena", 9.0), ("Jorge", 10.0)]

    mostrar("Grupo A (ordenado)", grupo_a)
    mostrar("Grupo B (ordenado)", grupo_b)

    ranking = intercalar(grupo_a, grupo_b, clave=lambda alumno: alumno[1])
    mostrar("Ranking general (intercalado)", ranking)