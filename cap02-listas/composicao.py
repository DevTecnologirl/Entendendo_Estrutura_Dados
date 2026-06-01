class Motor:
    def ligar(self):
        print("Motor ligado")

class Carro:
    def __init__(self):
        self.motor = Motor()
    def ligar_carro(self):
        self.motor.ligar()
        print("Carro pronto para andar")
carro = Carro()
carro.ligar_carro()
# Saída:
# Motor ligado
# Carro pronto para andar

# Relacionamento:
# Carro ---- tem um ----> Motor