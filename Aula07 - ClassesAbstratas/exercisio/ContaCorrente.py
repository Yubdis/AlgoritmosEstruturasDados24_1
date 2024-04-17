from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    
    def __init__(self, nome, valor):
        super().__init__(nome, valor)
        
    def depositar(self, valor):
        if (valor <= 0):
            print("Adicionar valor positivo")
        else:    
            print("Deposita recebeu")
            self.valor += valor
    def cadastrar(self, nome):
        self.nome = nome
    
    def imprimir(self):
        super().imprimir()
        print("Valor no Corrente: ", self.valor)