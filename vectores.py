import random


def mostrar_vector(datos):
    for dato in datos:
        print(dato)


def media(datos):
    suma = 0

    for dato in datos:
        suma = suma + dato

    return suma / len(datos)


def mediana(datos):
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)

    if n % 2 == 0:
        medio1 = datos_ordenados[n // 2 - 1]
        medio2 = datos_ordenados[n // 2]

        return (medio1 + medio2) / 2
    else:
        return datos_ordenados[n // 2]


def moda(datos):
    mayor = 0
    numero_moda = datos[0]

    for dato in datos:
        frecuencia = datos.count(dato)

        if frecuencia > mayor:
            mayor = frecuencia
            numero_moda = dato

    return numero_moda


def varianza(datos):
    promedio = media(datos)
    suma = 0

    for dato in datos:
        suma = suma + (dato - promedio) ** 2

    return suma / len(datos)


def desviacion_estandar(datos):
    return varianza(datos) ** 0.5


datos = []

for i in range(230):
    datos.append(random.randint(1, 100))


mostrar_vector(datos)

print("Media =", media(datos))
print("Mediana =", mediana(datos))
print("Moda =", moda(datos))
print("Varianza =", varianza(datos))
print("Desviación estándar =", desviacion_estandar(datos))

