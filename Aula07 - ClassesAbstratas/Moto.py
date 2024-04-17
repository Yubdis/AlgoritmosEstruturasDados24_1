from Veiculo import Veiculo

class Moto(Veiculo):
   
    def __init__(self, modelo, ano, cilindradas):
        super().__init__(modelo, ano)
        self.cilindradas = cilindradas
        
    def ligar(self, chave):
        if chave == "1234" : 
            print("Moto ligado")
        else:
            print("Não foi possível ligar o Moto")
            
    def imprimir(self):
        print("Motocicletá: ")
        super().imprimir()
        print("Cilindradas: ", self.cilindradas)