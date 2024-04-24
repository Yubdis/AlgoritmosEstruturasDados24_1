from abc import ABC, abstractclassmethod

# Uma classe abstrata chamada de Produto que contém os atributos/propriedades: 
# modelo, cor, preço e categoria. Esta classe possui um método getInformacoes() 
# que retorna todos os valores dos atributos. Esta classe também possui um método abstrato cadastrar().

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria
        
    def getInformacoes(self):
        print("Modelo: ", self.modelo)
        print("Cor: ", self.cor)
        print("Preço: ", self.preco)
        print("Categoria: ", self.categoria)
        
    @abstractclassmethod
    def cadastrar(self, nome):
        pass
    
# 2. O projeto também deve possuir as classes Desktop e Notebook que herdam da classe Produto. 
# A classe Desktop possui o atributo/propriedade fracamente privado potenciaDaFonte. 
# Esta classe reimplementa o método getInformacoes() herdado de Produto.



