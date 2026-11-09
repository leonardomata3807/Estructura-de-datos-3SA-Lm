
def kruskal(n, aristas):
    padre = list(range(n))

    def encontrar(x):
        if padre[x] != x:
            padre[x] = encontrar(padre[x])
        return padre[x]

    arbol = []
    costo_total = 0

    aristas.sort(key=lambda x: x[2])

    for u, v, peso in aristas:
        raiz_u = encontrar(u)
        raiz_v = encontrar(v)

        if raiz_u != raiz_v:
            padre[raiz_u] = raiz_v
            arbol.append((u, v, peso))
            costo_total += peso

    return arbol, costo_total


aristas = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

resultado, costo = kruskal(4, aristas)

print("Arbol de expansion minima:")
for arista in resultado:
    print(arista)

print("Costo total:", costo)
