#Tener una lista de números ordenados 
#Calcular el cuadrado de cada número y eliminar los cuadrados que estén fuera del rango [0, S^2].
#Devolverla lista de cuadrados filtrados en orden ascendente
def resultado(n, S):
    # Inicializamos un conjunto para almacenar los números al cuadrado únicos.
    numerosCuadrado = set()

    # Iteramos a través de los números originales.
    for num in n:
        # Calculamos el cuadrado del número.
        cuadrado = num ** 2

        # Verificamos si el cuadrado está dentro del rango [0, S*S].
        #Que el cuadrado sea mayor o igual que cero, asegurando que no tengamos números negativos en la lista resultante.
        if 0 <= cuadrado <= S * S:
            # Agregamos el cuadrado al conjunto para almacenar números únicos que cumplen con las condiciones.
            numerosCuadrado.add(cuadrado)

    # Devolvemos la lista de números al cuadrado filtrados y ordenados en orden ascendente.
    # Convertimos el conjunto en una lista y la ordenamos para obtener el resultado final.
    return sorted(numerosCuadrado, reverse=False)


print(resultado([1, 2, 3, 5, 6, 8, 9], 6))  # Resultado: [1, 4, 9, 25, 36]
print(resultado([-2, -1], 6))  # Resultado: [1, 4]
print(resultado([-6, -5, 0, 5, 6], 6))  # Resultado: [0, 25, 36]
print(resultado([-10, 10], 6))  # Resultado: []
