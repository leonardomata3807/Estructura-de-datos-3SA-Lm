
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


class Arbol:
    def __init__(self):
        self.raiz = None

   
    def insertar(self, dato):
        self.raiz = self._insertar(self.raiz, dato)

    def _insertar(self, nodo, dato):
        if nodo is None:
            return Nodo(dato)

        if dato < nodo.dato:
            nodo.izquierda = self._insertar(nodo.izquierda, dato)
        elif dato > nodo.dato:
            nodo.derecha = self._insertar(nodo.derecha, dato)

        return nodo

    
    def buscar(self, dato):
        return self._buscar(self.raiz, dato)

    def _buscar(self, nodo, dato):
        if nodo is None:
            return False

        if nodo.dato == dato:
            return True

        if dato < nodo.dato:
            return self._buscar(nodo.izquierda, dato)

        return self._buscar(nodo.derecha, dato)

 
    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izquierda)
            print(nodo.dato, end=" ")
            self.inorden(nodo.derecha)


    def preorden(self, nodo):
        if nodo:
            print(nodo.dato, end=" ")
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)


    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.dato, end=" ")


    def contar_nodos(self, nodo):
        if nodo is None:
            return 0

        return (1 + self.contar_nodos(nodo.izquierda)
                + self.contar_nodos(nodo.derecha))

   
    def altura(self, nodo):
        if nodo is None:
            return 0

        izquierda = self.altura(nodo.izquierda)
        derecha = self.altura(nodo.derecha)

        return 1 + max(izquierda, derecha)


    def eliminar(self, dato):
        self.raiz = self._eliminar(self.raiz, dato)

    def _eliminar(self, nodo, dato):
        if nodo is None:
            return None

        if dato < nodo.dato:
            nodo.izquierda = self._eliminar(nodo.izquierda, dato)

        elif dato > nodo.dato:
            nodo.derecha = self._eliminar(nodo.derecha, dato)

        else:
            if nodo.izquierda is None:
                return nodo.derecha

            if nodo.derecha is None:
                return nodo.izquierda

            sucesor = nodo.derecha
            while sucesor.izquierda:
                sucesor = sucesor.izquierda

            nodo.dato = sucesor.dato
            nodo.derecha = self._eliminar(
                nodo.derecha, sucesor.dato
            )

        return nodo



arbol = Arbol()

while True:
    print("\n--- MENU DE ARBOL BINARIO ---")
    print("1. Insertar elemento")
    print("2. Buscar elemento")
    print("3. Eliminar elemento")
    print("4. Recorrido inorden")
    print("5. Recorrido preorden")
    print("6. Recorrido postorden")
    print("7. Contar nodos")
    print("8. Mostrar altura")
    print("9. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        dato = int(input("Ingresa el numero: "))
        arbol.insertar(dato)
        print("Elemento insertado correctamente.")

    elif opcion == "2":
        dato = int(input("Numero a buscar: "))
        if arbol.buscar(dato):
            print("El elemento si existe en el arbol.")
        else:
            print("El elemento no existe.")

    elif opcion == "3":
        dato = int(input("Numero a eliminar: "))
        if arbol.buscar(dato):
            arbol.eliminar(dato)
            print("Elemento eliminado correctamente.")
        else:
            print("El elemento no existe.")

    elif opcion == "4":
        print("Recorrido inorden:")
        arbol.inorden(arbol.raiz)
        print()

    elif opcion == "5":
        print("Recorrido preorden:")
        arbol.preorden(arbol.raiz)
        print()

    elif opcion == "6":
        print("Recorrido postorden:")
        arbol.postorden(arbol.raiz)
        print()

    elif opcion == "7":
        print("Total de nodos:", arbol.contar_nodos(arbol.raiz))

    elif opcion == "8":
        print("Altura del arbol:", arbol.altura(arbol.raiz))

    elif opcion == "9":
        print("Programa finalizado.")
        break

    else:
        print("Opcion no valida.")
