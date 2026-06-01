class Lista:
    def exibir_tipo(self):
        print("Sou uma lista")


class Pilha(Lista):
    pass


class Fila(Lista):
    pass


pilha = Pilha()
fila = Fila()

pilha.exibir_tipo()
fila.exibir_tipo()