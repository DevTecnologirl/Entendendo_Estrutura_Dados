def minimo_maximo(array):
    menor = array[0]
    maior = array[0]
    
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
        if array[i] > maior:
            maior = array[i]
    return menor, maior

numeros = [13, 3, 45, 6, 61, 23]

menor, maior = minimo_maximo(numeros)

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")