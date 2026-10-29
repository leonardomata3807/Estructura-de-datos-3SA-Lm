postres = [
    ["Flan", ["huevo", "leche", "azucar"]],
    ["Gelatina", ["agua", "gelatina", "azucar"]],
    ["Flan", ["huevo", "leche", "vainilla"]],
    ["Arroz con leche", ["arroz", "leche", "canela"]],
    ["Gelatina", ["agua", "gelatina", "azucar"]]
]


def eliminar_repetidos(lista_postres):
    nombres_vistos = set()
    lista_nueva = []

    for postre in lista_postres:
        nombre = postre[0].strip().lower()

        if nombre not in nombres_vistos:
            nombres_vistos.add(nombre)
            lista_nueva.append(postre)

    return lista_nueva


print("POSTRES ANTES DE ELIMINAR REPETIDOS:")

for postre in postres:
    print(postre)


postres = eliminar_repetidos(postres)


print("\nPOSTRES DESPUES DE ELIMINAR REPETIDOS:")

for postre in postres:
    print(postre)