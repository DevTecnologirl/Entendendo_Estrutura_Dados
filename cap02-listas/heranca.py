class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def dormir(self):
        print(f"{self.nome} esta dormindo")

class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} esta larindo")
        
dog = Cachorro("Rex")
dog.dormir() # herdado de Animal
dog.latir() #proprio de Cachorro
# Hierarquia: É UM
# Animal
#    ↑
# Cachorro