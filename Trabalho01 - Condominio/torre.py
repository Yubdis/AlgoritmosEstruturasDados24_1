class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        
    def __str__(self):
        texto = "\nID: " + self.id 
        texto += "\nNome: " + self.nome
        texto += "\nEndereco: " + self.endereco
        return texto
    
    def cadastrar():
        pass
    
    def imprimir(self):
        print("-------Torre------")
        print(self)
    