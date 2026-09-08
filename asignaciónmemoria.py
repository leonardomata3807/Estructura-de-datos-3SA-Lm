print("MEMORIA ESTÁTICA")

calificaciones = [0] * 5

for i in range(5):
    calificaciones[i] = int(
        input(f"Captura la calificación {i + 1}: ")
    )

print("\nCalificaciones:")
print(calificaciones)




print("\nMEMORIA DINÁMICA")

frutas = []

frutas.append("Mango")
frutas.append("Manzana")
frutas.append("Banana")
frutas.append("Uvas")

print("Lista inicial:")
print(frutas)

frutas.pop(0)
frutas.pop(1)

frutas.append("Sandía")

print("\nLista después de modificarla:")
print(frutas)
