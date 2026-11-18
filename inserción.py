
numeros = [7, 4, 9, 2, 6, 1]

print("Lista original:", numeros)

for i in range(1, len(numeros)):
    actual = numeros[i]
    j = i - 1

    while j >= 0 and numeros[j] > actual:
        numeros[j + 1] = numeros[j]
        j -= 1

    numeros[j + 1] = actual

print("Lista ordenada:", numeros)
