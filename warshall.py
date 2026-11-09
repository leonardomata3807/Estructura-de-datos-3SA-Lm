
def warshall(grafo):
    n = len(grafo)

    alcance = [fila[:] for fila in grafo]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                alcance[i][j] = (
                    alcance[i][j] or
                    (alcance[i][k] and alcance[k][j])
                )

    return alcance


grafo = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

resultado = warshall(grafo)

print("Matriz de alcanzabilidad:")
for fila in resultado:
    print(fila)
