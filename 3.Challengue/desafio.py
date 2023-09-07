#Ejercicio de la tienda
def vueltasMinimas(moneda):
    # Ordenamos las monedas en orden ascendente.
    moneda.sort()

    # Inicializamos una variable para llevar el seguimiento del cambio mínimo.
    minVueltas = 1

    # Iteramos a través de las monedas y verificamos si podemos construir el cambio mínimo actual.
    for money in moneda:
        if money <= minVueltas:
            minVueltas += money
        else:
            break

    return minVueltas

# Ejemplos de uso:
print(vueltasMinimas([5, 7, 1, 1, 2, 3, 22]))  # Resultado: 20
print(vueltasMinimas([1, 1, 1, 1, 1]))  # Resultado: 6
print(vueltasMinimas([1, 5, 1, 1, 1, 10, 15, 20, 100]))  # Resultado: 55
