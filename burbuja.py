
numeros = [8, 3, 5, 1, 9, 2]

print("Lista original:", numeros)

n = len(numeros)

for i in range(n):
    for j in range(0, n - i - 1):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Lista ordenada:", numeros)
