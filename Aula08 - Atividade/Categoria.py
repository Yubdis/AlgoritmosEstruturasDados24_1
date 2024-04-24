# 1. Construir código necessário em Python para implementar o seguinte 
# projeto: Uma classe Categoria que possui os atributos id e nome. 
# Uma classe abstrata chamada de Produto que contém os atributos/propriedades: 
# modelo, cor, preço e categoria. Esta classe possui um método getInformacoes() 
# que retorna todos os valores dos atributos. Esta classe também possui um método abstrato cadastrar().

class Categoria():
    def __init__(self, nome = "Outra"):
        self.id = None
        self.nome = nome