class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao


class ListaTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)


lista = ListaTarefas()

lista.adicionar(Tarefa("Estudar Arrays"))
lista.adicionar(Tarefa("Resolver exercícios"))

for tarefa in lista.tarefas:
    print(tarefa.descricao)