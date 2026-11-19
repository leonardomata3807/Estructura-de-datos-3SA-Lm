
def radix_sort(lista):
    if any(numero < 0 for numero in lista):
        raise ValueError("No se aceptan números negativos.")

    resultado = lista.copy()

    if not resultado:
        return resultado

    maximo = max(resultado)
    exp = 1

    while maximo // exp > 0:
        salida = [0] * len(resultado)
        conteo = [0] * 10

        for numero in resultado:
            digito = (numero // exp) % 10
            conteo[digito] += 1

        for i in range(1, 10):
            conteo[i] += conteo[i - 1]

        for i in range(len(resultado) - 1, -1, -1):
            digito = (resultado[i] // exp) % 10
            salida[conteo[digito] - 1] = resultado[i]
            conteo[digito] -= 1

        resultado = salida
        exp *= 10

    return resultado


while True:
    print("\n--- RADIX SORT ---")
    print("1. Ordenar números")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        try:
            cantidad = int(input("¿Cuántos números deseas ingresar? "))

            if cantidad <= 0:
                print("Ingresa una cantidad mayor que cero.")
                continue

            numeros = []

            for i in range(cantidad):
                numero = int(input(f"Número {i + 1}: "))
                numeros.append(numero)

            print("Lista original:", numeros)
            print("Lista ordenada:", radix_sort(numeros))

        except ValueError as error:
            print("Error:", error)

    elif opcion == "2":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
