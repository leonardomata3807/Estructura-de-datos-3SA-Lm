
import heapq

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    cola = [(0, inicio)]

    while cola:
        distancia, nodo = heapq.heappop(cola)

        if distancia > distancias[nodo]:
            continue

        for vecino, peso in grafo[nodo]:
            nueva_distancia = distancia + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                heapq.heappush(
                    cola, (nueva_distancia, vecino)
                )

    return distancias


grafo = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8)],
    'D': [('B', 5), ('C', 8)]
}

resultado = dijkstra(grafo, 'A')

print("Distancias desde A:")
for nodo, distancia in resultado.items():
    print(nodo, ":", distancia)
