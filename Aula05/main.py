from Categoria import Categoria
from Veiculo import Veiculo
from Carro import Carro
from Moto import Moto

cat1 = Categoria()
cat2 = Categoria("Esportiva")
# cat3 = Categoria("SUV")

v1 = Veiculo()
v1.imprimir()

c1 = Carro("Jeep", 2021, Categoria("SUV"), 4 )
c1.imprimir()

m1 = Moto("Honda", 2020, cat2, 250)
m1.imprimir()
