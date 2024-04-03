from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro=False):
        super().__init__(marca, qtdRodas, modelo)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro
        
    def __str__(self):
        return super().__str__() + "\nNumero Marchas: " + str(self.numMarchas) + "\nBagageiro: " + self.bagageiro
    
    def imprimirInformacoes(self):
        print(self)