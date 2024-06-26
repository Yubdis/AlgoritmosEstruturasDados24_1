from torre import Torre

class Apartamento(Torre):
    def __init__(self, id, numero, torre, vaga=None):
        super().__init__(id)
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = None
        
    def __str__(self):
        texto = "\nNome: " + self.id.nome
        texto = "\nNumero: " + self.numero
        texto += "\nTorre " + self.torre
        texto += "\nVaga: " + self.vaga
        return texto

    
    def cadastrar():
        pass
    
    def imprimir(self):
        print(self)