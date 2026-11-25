def fusionar_bloques(b1, b2, clave):
    
    res, i, j = [], 0, 0
    while i < len(b1) and j < len(b2):
        if clave(b1[i]) <= clave(b2[j]):
            res.append(b1[i]); i += 1
        else:
            res.append(b2[j]); j += 1
    res.extend(b1[i:])
    res.extend(b2[j:])
    return res


def mezcla_directa(f0, clave=lambda x: x, verbose=True):
    n = len(f0)
    tam = 1
    pasada = 1

    while tam < n:
       
        f1, f2 = [], []
        for inicio in range(0, n, tam):
            bloque = f0[inicio:inicio + tam]
            if (inicio // tam) % 2 == 0:
                f1.extend(bloque)
            else:
                f2.extend(bloque)

       
        f0 = []
        for inicio in range(0, max(len(f1), len(f2)), tam):
            b1 = f1[inicio:inicio + tam]
            b2 = f2[inicio:inicio + tam]
            f0.extend(fusionar_bloques(b1, b2, clave))

        if verbose:
            print(f"\nPasada {pasada} (bloques de {tam})")
            print("  F1:", [p[2] for p in f1])
            print("  F2:", [p[2] for p in f2])
            print("  F0:", [p[2] for p in f0])

        tam *= 2
        pasada += 1

    return f0


if __name__ == "__main__":
   
    pedidos = [
        (101, "Ana",    850), (102, "Luis",   120), (103, "Marta",  430),
        (104, "Pedro", 1500), (105, "Sofía",  275), (106, "Carlos", 990),
        (107, "Elena",  60),  (108, "Jorge",  640),
    ]

    print("Pedidos originales (monto):", [p[2] for p in pedidos])
    ordenados = mezcla_directa(pedidos, clave=lambda p: p[2])

    print("\nPedidos ordenados por monto")
    print("-" * 36)
    for folio, cliente, monto in ordenados:
        print(f"{folio}  {cliente:<8} ${monto:>6}")