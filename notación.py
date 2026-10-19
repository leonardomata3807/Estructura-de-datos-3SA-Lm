
class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, dato):
        self.elementos.append(dato)

    def desapilar(self):
        if len(self.elementos) > 0:
            return self.elementos.pop()
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0


def evaluar(expresion):
    pila = Pila()
    elementos = expresion.split()

    for elemento in elementos:
        if elemento not in ["+", "-", "*", "/", "^"]:
            pila.apilar(float(elemento))
        else:
            b = pila.desapilar()
            a = pila.desapilar()

            if a is None or b is None:
                return "Expresion incorrecta"

            if elemento == "+":
                resultado = a + b
            elif elemento == "-":
                resultado = a - b
            elif elemento == "*":
                resultado = a * b
            elif elemento == "/":
                if b == 0:
                    return "No se puede dividir entre cero"
                resultado = a / b
            elif elemento == "^":
                resultado = a ** b

            pila.apilar(resultado)

    if len(pila.elementos) == 1:
        return pila.desapilar()
    else:
        return "Expresion incorrecta"


expresion = input("Escribe la expresion posfija (ejemplo: 5 3 +): ")

print("Resultado:", evaluar(expresion))
