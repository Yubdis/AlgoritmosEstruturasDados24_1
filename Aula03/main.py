from Pessoa import Pessoa
from Cidade import Cidade
from Classes import *

c1 = Cidade("POA")
p1 = Pessoa("João")
p2 = Pessoa("Maria")
p2.cidade = p1.cidade
print(p1.cidade)
print(p2.cidade)

print("---------------------------")
c2 = Cidade()
c3 = Cidade("Capão de Canoa")

p3 = Pessoa("Júlia")
p4 = Pessoa("Carlos", 20)
p5 = Pessoa("Suzy", 40, c2)

print("=========================")

ped1 = Pedido("Duque de caxias", p1)

print(ped1.cliente)