
numeros = [10, 5, 8, 3, 6, 1]

print("Lista original:", numeros)

n = len(numeros)

for i in range(n):
    minimo = i

    for j in range(i + 1, n):
        if numeros[j] < numeros[minimo]:
            minimo = j

    numeros[i], numeros[minimo] = numeros[minimo], numeros[i]

print("Lista ordenada:", numeros)
