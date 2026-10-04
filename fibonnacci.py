# Programa para mostrar la serie de Fibonacci

cantidad = int(input("¿Cuántos números de Fibonacci quieres mostrar? "))

a = 0
b = 1

print("Serie de Fibonacci:")

for i in range(cantidad):
    print(a, end=" ")
    
    siguiente = a + b
    a = b
    b = siguiente