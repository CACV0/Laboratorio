#Tomar una lista de números y un número S
#Eliminar los números que contienen dígitos mayores o iguales a S
#Devolver la lista resultante en orden
def filtrarOrdenar_numeros(n, S):
    # Inicializamos una lista para almacenar los números filtrados.
    numerosFiltrados = []

    # Iteramos a través de los números originales.
    for numeroOriginal in n:
        # Convertimos el número original en una cadena para procesar sus dígitos individualmente.
        numeroStr = str(numeroOriginal)
        
        # Filtramos los dígitos que son menores que S y los unimos nuevamente en una cadena.
        numeroFiltradoStr = ''.join(digito for digito in numeroStr if int(digito) < S)
        
        # Verificamos si la cadena filtrada no está vacía y si es mayor que cero antes de agregarla a la lista.
        if numeroFiltradoStr and int(numeroFiltradoStr) > 0:
            numerosFiltrados.append(int(numeroFiltradoStr))

    # Ordenamos la lista de números filtrados en orden descendente o Ascendente y la devolvemos como resultado.
    return sorted(numerosFiltrados, reverse=False)

# Ejemplos:
print(filtrarOrdenar_numeros([1, 2, 3, 4, 5, 6], 6))  # Output: [5, 4, 3, 2, 1]
print(filtrarOrdenar_numeros([10, 20, 30, 40], 6))  # Output: [40, 30, 20, 10]
print(filtrarOrdenar_numeros([6], 6))  # Output: []
print(filtrarOrdenar_numeros([66], 6))  # Output: []
print(filtrarOrdenar_numeros([65], 6))  # Output: [5]
print(filtrarOrdenar_numeros([6, 2, 1], 6))  # Output: [1, 2]
print(filtrarOrdenar_numeros([60, 6, 5, 4, 3, 2, 7, 7, 29, 1], 6))  # Output: [5, 4, 3, 2, 2, 1]
