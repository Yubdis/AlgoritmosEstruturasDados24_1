from No import No


class ListaDuplamente:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
            self.fim = nodo
        else:
            if nodo.dado < self.inicio.dado:
                nodo.proximo = self.inicio
                self.inicio.anterior = nodo
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux:
                    if nodo.dado < aux.dado:
                        nodo.proximo = ant.proximo  # nodo.proximo = aux
                        ant.proximo = nodo
                        nodo.anterior = ant # nodo.anterior = aux.anterior
                        aux.anterior = nodo
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
                if aux == None and nodo.dado >= ant.dado:
                    ant.proximo = nodo
                    nodo.anterior = ant
                    self.fim = nodo
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        print("------Lista Encadeada--------------------------")
        if self.inicio == None:
            print("Lista Vazia")
        else:
            print(self.tamanho, " elementos na Lista")
            aux = self.inicio
            while aux:
                print(aux.dado)
                aux = aux.proximo
    
    def imprimirReverso(self):
        print("------Lista Duplamente Encadeada--------------------------")
        if self.inicio == None:
            print("Lista Vazia")
        else:
            print(self.tamanho, " elementos na Lista")
            aux = self.fim
            while aux:
                print(aux.dado)
                aux = aux.anterior
                
    def remover(self, valor):
        tamInicial = self.tamanho
        if self.inicio != None:

            # Se valor é igual ao primeiro elemento
            if self.inicio.dado == valor:
                self.inicio = self.inicio.proximo
                if self.inicio == None:
                    self.fim = None
                else:
                    self.inicio.anterior = None
                self.tamanho -= 1
                return

            # Lista com vários elementos e o valor não está no primeiro
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux:
                    if aux.dado == valor:
                        if aux.proximo == None:
                            self.fim = ant
                        else:
                            aux.proximo.anterior = ant    
                        ant.proximo = aux.proximo
                        
                        self.tamanho -= 1
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
            if tamInicial == self.tamanho:
                print("Valor não encontrado")
        self.imprimir()

    def reverseList(self):
        temp = None
        current = self.inicio

        while current is not None:
            temp = current.antes
            current.antes = current.proximo
            current.proximo = temp
            current = current.antes

        if temp is not None:
            self.head = temp.antes
