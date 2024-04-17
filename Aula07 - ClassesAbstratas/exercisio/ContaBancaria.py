from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        
    def cadastrar(self, nome):
        self.nome = nome
    
    @abstractmethod
    def depositar(self, valor):
        pass
    
    def imprimir(self):
        print("Nome do Conta: ", self.nome)