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


class Apartamento(Torre):
    def __init__(self, id, numero, torre, vaga=None):
        super().__init__(id)
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = None

    def __str__(self):
        texto = "\nNome: " + self.id.nome
        texto = "\nNumero: " + self.numero
        texto += "\nTorre " + self.torre
        texto += "\nVaga: " + self.vaga
        return texto

    def cadastrar():
        pass

    def imprimir(self):
        print(self)


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
