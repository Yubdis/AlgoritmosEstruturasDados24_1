from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, potencialDoMotor):
        super().__init__(marca, qtdRodas, modelo)
        self.potencialDoMotor = potencialDoMotor
    
    def __str__(self):
        return super().__str__() + "\nPotential Do Motor: " + str( self.potencialDoMotor )
    
    def imprimirInformacoes(self):
        print(self)