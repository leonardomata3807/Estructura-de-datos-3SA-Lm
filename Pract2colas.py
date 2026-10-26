class Order:
    """Representa un pedido."""
    def __init__(self, qtty, customer):
        self.__customer = customer
        self.__qtty = qtty

    def print(self):
        print("     Customer:", self.get_customer())
        print("     Quantity:", self.get_qtty())
        print("     ------------")

    def get_qtty(self):
        return self.__qtty

    def get_customer(self):
        return self.__customer


class Node:
    """Nodo de la lista enlazada: guarda un objeto (info) y el siguiente nodo."""
    def __init__(self, info):
        self.info = info
        self.next = None

    def get_info(self):
        return self.info

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class Queue:
    """Cola FIFO con lista enlazada. top = cabeza, tail = último nodo."""
    def __init__(self):
        self.top = None
        self.tail = None
        self._size = 0

    def size(self):
        return self._size

    def is_empty(self):
        return self.top is None

    def front(self):
        """Devuelve el primer elemento sin quitarlo. None si está vacía."""
        if self.is_empty():
            return None
        return self.top.info

    def enqueue(self, info):
        """Agrega un elemento al final."""
        new_node = Node(info)
        if self.is_empty():
            self.top = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self._size += 1

    def dequeue(self):
        """Devuelve y quita el primer elemento. None si está vacía."""
        if self.is_empty():
            return None
        info = self.top.info
        self.top = self.top.next
        if self.top is None:
            self.tail = None
        self._size -= 1
        return info

    def print_info(self):
        print("********* QUEUE DUMP *********")
        print("   Size:", self._size)
        node = self.top
        i = 1
        while node is not None:
            print("   ** Element", i)
            node.info.print()
            node = node.next
            i += 1
        print("******************************")

    def get_nth(self, pos):
        """Devuelve el n-ésimo elemento (1 = primero) sin borrarlo.
        None si la posición no es válida."""
        if pos < 1 or pos > self._size:
            return None
        node = self.top
        for _ in range(pos - 1):
            node = node.next
        return node.info


# ---------- TestQueue ----------
if __name__ == "__main__":
    cola = Queue()

    o1 = Order(20, "cust1")
    o2 = Order(30, "cust2")
    o3 = Order(40, "cust3")
    o4 = Order(50, "cust3")

    print(">>> Cola vacía")
    cola.print_info()

    print(">>> Enqueue de 3 pedidos")
    cola.enqueue(o1)
    cola.print_info()
    cola.enqueue(o2)
    cola.print_info()
    cola.enqueue(o3)
    cola.print_info()

    print(">>> front()")
    print("   Primero en la cola:")
    cola.front().print()
    cola.print_info()

    print(">>> dequeue()")
    sacado = cola.dequeue()
    print("   Elemento extraído:")
    sacado.print()
    cola.print_info()

    print(">>> Vaciando la cola")
    cola.dequeue()
    cola.dequeue()
    cola.print_info()
    print("dequeue en cola vacía:", cola.dequeue())
    print("front en cola vacía:", cola.front())

    print(">>> getNth: 4 elementos, obtener el tercero")
    for o in (o1, o2, o3, o4):
        cola.enqueue(o)
    cola.print_info()
    tercero = cola.get_nth(3)
    print("   Elemento 3:")
    tercero.print()
    print("   Posición 0 (inválida):", cola.get_nth(0))
    print("   Posición 9 (inválida):", cola.get_nth(9))