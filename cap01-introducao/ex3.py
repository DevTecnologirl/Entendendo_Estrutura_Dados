#busca simples
def buscar(lista,valor):
    for i in range(len(lista)):
        if lista[i] ==valor:
            return i
        return -1
numeros = [10,20,30,40,50,60]
print(buscar(numeros, 30)) #2
print(buscar(numeros, 99)) #-1