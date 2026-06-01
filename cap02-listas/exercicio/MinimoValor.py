def minimo(array):
    menor = array[0]
    posicao = 0

    for indice in range(len(array)):
        if array[indice] < menor:
            menor = array[indice]
            posicao = indice

    return menor, posicao