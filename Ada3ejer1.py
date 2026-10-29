postres = [
    ["Arroz con leche", ["arroz", "leche", "azucar", "canela"]],
    ["Flan", ["huevo", "leche", "azucar", "vainilla"]],
    ["Gelatina", ["agua", "gelatina", "azucar"]],
    ["Pastel de chocolate", ["harina", "huevo", "chocolate", "azucar"]],
    ["Pay de limon", ["galletas", "limon", "leche condensada"]]
]


def ordenar_postres():
    postres.sort(key=lambda postre: postre[0].lower())


def buscar_postre(nombre):
    for postre in postres:
        if postre[0].lower() == nombre.lower():
            return postre
    return None


def mostrar_ingredientes():
    nombre = input("Nombre del postre: ").strip()
    postre = buscar_postre(nombre)

    if postre is None:
        print("Error: el postre no existe.")
    elif len(postre[1]) == 0:
        print("El postre no tiene ingredientes registrados.")
    else:
        print("Ingredientes de", postre[0] + ":")
        for ingrediente in postre[1]:
            print("-", ingrediente)


def agregar_ingredientes():
    nombre = input("Nombre del postre: ").strip()
    postre = buscar_postre(nombre)

    if postre is None:
        print("Error: el postre no existe.")
        return

    entrada = input("Ingredientes nuevos separados por comas: ")
    ingredientes = entrada.split(",")
    agregados = 0

    for ingrediente in ingredientes:
        ingrediente = ingrediente.strip()

        if ingrediente == "":
            continue

        if ingrediente.lower() in [i.lower() for i in postre[1]]:
            print("El ingrediente ya existe:", ingrediente)
        else:
            postre[1].append(ingrediente)
            agregados += 1

    if agregados > 0:
        print("Ingredientes agregados correctamente.")
    else:
        print("No se agregaron ingredientes.")


def eliminar_ingrediente():
    nombre = input("Nombre del postre: ").strip()
    postre = buscar_postre(nombre)

    if postre is None:
        print("Error: el postre no existe.")
        return

    if len(postre[1]) == 0:
        print("El postre no tiene ingredientes.")
        return

    ingrediente = input("Ingrediente que desea eliminar: ").strip()

    for i in range(len(postre[1])):
        if postre[1][i].lower() == ingrediente.lower():
            del postre[1][i]
            print("Ingrediente eliminado correctamente.")
            return

    print("Error: el ingrediente no existe en este postre.")


def alta_postre():
    nombre = input("Nombre del nuevo postre: ").strip()

    if nombre == "":
        print("Error: el nombre no puede estar vacio.")
        return

    if buscar_postre(nombre) is not None:
        print("Error: el postre ya esta registrado.")
        return

    entrada = input("Ingredientes separados por comas: ")
    ingredientes = []

    for ingrediente in entrada.split(","):
        ingrediente = ingrediente.strip()

        if ingrediente != "":
            if ingrediente.lower() not in [i.lower() for i in ingredientes]:
                ingredientes.append(ingrediente)

    postres.append([nombre, ingredientes])
    ordenar_postres()

    print("Postre registrado correctamente.")


def baja_postre():
    nombre = input("Nombre del postre que desea eliminar: ").strip()
    postre = buscar_postre(nombre)

    if postre is None:
        print("Error: el postre no existe.")
        return

    postres.remove(postre)
    print("Postre y todos sus ingredientes eliminados correctamente.")

def mostrar_postres():
    if len(postres) == 0:
        print("No hay postres registrados.")
        return

    print("\nLista de postres:")

    for postre in postres:
        print("-", postre[0])

def menu():
    while True:
        print("\n===== MENU DE POSTRES =====")
        print("1. Mostrar ingredientes")
        print("2. Agregar ingredientes")
        print("3. Eliminar ingrediente")
        print("4. Dar de alta un postre")
        print("5. Dar de baja un postre")
        print("6. Mostrar todos los postres")
        print("7. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            mostrar_ingredientes()
        elif opcion == "2":
            agregar_ingredientes()
        elif opcion == "3":
            eliminar_ingrediente()
        elif opcion == "4":
            alta_postre()
        elif opcion == "5":
            baja_postre()
        elif opcion == "6":
            mostrar_postres()
        elif opcion == "7":
            print("Programa terminado.")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")


menu()