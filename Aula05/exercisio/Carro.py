from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potencialDoMotor, qtdPortas):
        super().__init__(marca, qtdRodas, modelo, potencialDoMotor)
        self.qtdPortas = qtdPortas
        
    def __str__(self):
        return super().__str__() + "\nPortas: " + str(self.qtdPortas)
    
    def imprimirInformacoes(self):
        print(self)