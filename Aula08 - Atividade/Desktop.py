from Produto import *

# 2. O projeto também deve possuir as classes Desktop e Notebook que herdam da classe Produto.
# A classe Desktop possui o atributo/propriedade fracamente privado potenciaDaFonte.
# Esta classe reimplementa o método getInformacoes() herdado de Produto.

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potencialDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potencialDaFonte = potencialDaFonte

    def getInformacoes(self):
        print("=====Desktop=====")
        super().getInformacoes()
        print("\nPotencial Da Fonte: " + str(self.getPotencialDeBateria()) )

    def getPotencialDeBateria(self):
        return self._potencialDaFonte

    def setPotencialDeBateria(self, valor):
        self._potencialDaFonte = valor

    def cadastrar(self, nome):
        print("Desktop Registrou para: " + nome)