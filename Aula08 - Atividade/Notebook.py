from Produto import Produto

# 2. O projeto também deve possuir as classes Desktop e Notebook que herdam da classe Produto. 
# A classe Desktop possui o atributo/propriedade fracamente privado potenciaDaFonte. 
# Esta classe reimplementa o método getInformacoes() herdado de Produto.

# 3. A classe Notebook possui o atributo/propriedade fortemente privado tempoDeBateria. 
# Esta classe reimplementa o método getInformacoes() herdado de Produto. 
# Construa getters e setters para os atributos que não forem públicos. 
# Todas as classes devem ter um método construtor.

class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria
        
    def getInformacoes(self):
        super().getInformacoes()
        print("Tempo De Bateria: "+ str(self.getTempoDeBateria))
        
    def getTempoDeBateria(self):
        return self.__tempoDeBateria
        
    def setTempoDeBateria(self, valor):
        self.__tempoDeBateria = valor
    
    def cadastrar(self, nome):
        print("Notebook Registrou para: " + nome)
