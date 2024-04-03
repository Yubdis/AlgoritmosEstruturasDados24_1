from Automovel import Automovel

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potencialDoMotor, partidaEletrica=False):
        super().__init__(marca, qtdRodas, modelo, potencialDoMotor)
        self.partidaEletrica = partidaEletrica
        
    def __str__(self):
        return super().__str__() + "\nPartida Eletrica: " + str(self.partidaEletrica)
    
    def imprimirInformacoes(self):
        print(self)