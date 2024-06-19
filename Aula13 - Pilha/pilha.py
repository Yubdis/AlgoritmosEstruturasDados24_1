from livro import Livro  # Assuming Livro class is defined in livro module

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0  # Initialize tamanho to 0 for an empty stack

    def add(self, titulo, autor, paginas):
        livro = Livro(titulo, autor, paginas)
        livro.proximo = self.topo
        self.topo = livro
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        print("------ Pilha de Livros ------")
        if self.topo is None:
            print("Pilha Vazia")
        else:
            print(self.tamanho, " elementos na Pilha")
            aux = self.topo
            while aux:
                print(aux.titulo)
                aux = aux.proximo
    
    def remover(self):
        if self.topo:
            self.topo = self.topo.proximo
            self.tamanho -= 1
        else:
            print("Pilha está vazia")
        
        self.imprimir()
