from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, ano, cat, cilindradas):
        super().__init__(marca, ano, cat)
        self.cilindradas = cilindradas
        
    def __str__(self):
        texto = "\nMoto: \nMarca: " + self.marca +"\nAno: " + str( self.ano )
        texto += "\nCategoria: " + self.categoria.nome
        texto += "\nCilindradas: " + str( self.cilindradas )
        return texto 
    
    def imprimir(self):
        print(self)
