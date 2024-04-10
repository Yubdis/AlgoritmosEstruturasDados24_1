class Pessoa:
    def __init__(self, nome, endereco):
        self.__codigo = None
        self.nome = nome
        self._endereco = endereco
        self.__telefone = None
        
    def imprimeNome(self):
        return self.nome
    
    def imprimeTelefone(self):
        return self.__telefone
    
    
class Fisica(Pessoa):
    def __init__(self, nome, endereco, idade, peso, altura):
        super().__init__(nome, endereco)
        self.__cpf = None
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def imprimeCPF(self):
        return self.__cpf
    
    def calculaMC():
        pass
    

class Juridica(Pessoa):
    def __init__(self, nome, endereco, quantidadeFuncionarios):
        super().__init__(nome, endereco)
        self.quantidadeFuncionarios = quantidadeFuncionarios
        self.__CNPJ = None
        self.__inscricaoEstadual = None
        
    def imprimeCNPJ(self):
        return self.__CNPJ
    
    def emitirNotaFiscal(self):
        pass