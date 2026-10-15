
def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print("Mover disco de", origen, "a", destino)
    else:
        hanoi(n - 1, origen, destino, auxiliar)
        print("Mover disco de", origen, "a", destino)
        hanoi(n - 1, auxiliar, origen, destino)


discos = int(input("Ingresa el numero de discos: "))

hanoi(discos, "A", "B", "C")
