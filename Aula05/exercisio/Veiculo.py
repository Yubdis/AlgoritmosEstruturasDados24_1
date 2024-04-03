class Veiculo:
    def __init__(self, marca, qtdRodas, modelo):
        self.id = None
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = 0
        
    def __str__(self):
        texto = "\nVeículo: "
        texto += "\nMarca: " + self.marca 
        texto += "\nqtdRodas: " + str( self.qtdRodas )
        texto += "\nModelo: " + self.modelo
        texto += "\nVelocidade: " + str( self.velocidade )
        return texto
        
    def imprimirInformacoes(self):
        print(self)
        
    def acelerar(self, num):
        self.velocidade += num
        
    def frear(self, num):
        self.velocidade -= num
        
        
        
        
        
         