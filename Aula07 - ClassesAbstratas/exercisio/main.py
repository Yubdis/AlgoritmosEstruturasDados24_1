from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

c1 = ContaCorrente("Simon", 200)
c1.depositar(100)
c1.imprimir()

print("\n=============================\n")

p1 = ContaPoupanca("Dave", 400)
p1.depositar(300)
p1.imprimir()

p1.cadastrar("Bill")
p1.imprimir()