def valor_minimo(array):
    menor = array[0]
    indice_menor = 0
    
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            indice_menor = i
    return menor, indice_menor

numeros = [15, 8, 9, 20, 12, 7]

valor, indice = valor_minimo(numeros)

print(f"Menor valor: {valor}")
print(f"Menor indice {indice}")