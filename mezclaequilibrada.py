def separar_corridas(datos):

    if not datos:
        return []
    corridas, actual = [], [datos[0]]
    for x in datos[1:]:
        if x >= actual[-1]:
            actual.append(x)
        else:
            corridas.append(actual)
            actual = [x]
    corridas.append(actual)
    return corridas


def mezclar(c1, c2):
    
    res, i, j = [], 0, 0
    while i < len(c1) and j < len(c2):
        if c1[i] <= c2[j]:
            res.append(c1[i]); i += 1
        else:
            res.append(c2[j]); j += 1
    res.extend(c1[i:])
    res.extend(c2[j:])
    return res


def mezcla_equilibrada(datos, verbose=True):
    corridas = separar_corridas(datos)

    
    f1 = corridas[0::2]
    f2 = corridas[1::2]
    if verbose:
        print("Distribución inicial")
        print("  F1:", f1)
        print("  F2:", f2)

    fase = 1
    while len(f1) + len(f2) > 1:
        f3, f4 = [], []
        destino = f3
       
        while f1 or f2:
            c1 = f1.pop(0) if f1 else []
            c2 = f2.pop(0) if f2 else []
            destino.append(mezclar(c1, c2))
            destino = f4 if destino is f3 else f3

        if verbose:
            print(f"\nFase {fase}")
            print("  F3:", f3)
            print("  F4:", f4)

        
        f1, f2 = f3, f4
        fase += 1

    return f1[0] if f1 else (f2[0] if f2 else [])


if __name__ == "__main__":
    temperaturas = [22, 25, 30, 18, 21, 27, 15, 19, 24, 31, 12, 16, 20, 14, 26]
    print("Datos originales:", temperaturas, "\n")

    resultado = mezcla_equilibrada(temperaturas)
    print("\nDatos ordenados:", resultado)