from Pessoa import Pessoa

class Pedido:
    def __init__(self, endereco, cliente = Pessoa("Simon")):
        self.id = None
        self.endereco = endereco
        self.produtos = []
        self.cliente = cliente

    def addProduto(self, produto):
        self.produtos.append(produto)
        soma = 0
        for produto in self.produtos:
            soma += produto.preco
        return soma

class Produto:
    def __init__(self, nome, preco, qtd, cat):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.categoria = cat

class Categoria:
    def __init__(self, nome):
        self.id = None
        self.nome = nome