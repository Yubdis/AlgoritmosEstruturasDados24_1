from apartamento import Apartamento
# 2) Este condomínio, não possui vagas de garagem para todos os apartamentos. 
# Isso faz com que exista uma fila de espera por vagas. Implemente uma fila de espera que contenha 
# os métodos para adicionar apartamentos na fila, retirar apartamentos informando o número da vaga 
# que este apartamento receberá e um método para imprimir a fila de espera.

class FilaEspera:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def add(self, vaga):
        nodo = Apartamento(vaga)
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.proximo = nodo
        self.fim = nodo
        self.tamanho += 1
        self.imprimir()
    
    def imprimir(self):
        print("------Fila Espera Vaga-----------")
        if self.inicio == None:
            print("Fila Vazia")
        else:
            print(self.tamanho, " pessoas na Fila")
            aux = self.inicio
            texto = ""
            while aux:
                texto += aux.dado + " - "
                aux = aux.proximo
            print(texto)
            
    def remover(self):
        if self.inicio:
            self.inicio = self.inicio.proximo
            if self.inicio != None:
                self.fim = None
            self.tamanho -= 1
        self.imprimir()