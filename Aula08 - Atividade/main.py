from Categoria import Categoria
from Produto import Produto
from Desktop import Desktop
from Notebook import Notebook
# 1. Construir código necessário em Python para implementar o seguinte 
# projeto: Uma classe Categoria que possui os atributos id e nome. 
# Uma classe abstrata chamada de Produto que contém os atributos/propriedades: 
# modelo, cor, preço e categoria. Esta classe possui um método getInformacoes() 
# que retorna todos os valores dos atributos. Esta classe também possui um método abstrato cadastrar().

# 2. O projeto também deve possuir as classes Desktop e Notebook que herdam da classe Produto. 
# A classe Desktop possui o atributo/propriedade fracamente privado potenciaDaFonte. 
# Esta classe reimplementa o método getInformacoes() herdado de Produto.

# 3. A classe Notebook possui o atributo/propriedade fortemente privado tempoDeBateria. 
# Esta classe reimplementa o método getInformacoes() herdado de Produto. 
# Construa getters e setters para os atributos que não forem públicos. 
# Todas as classes devem ter um método construtor.

# 4. Construa um arquivo do tipo main com a utilização das classes construídas, 
# para teste dos algoritmos.

# 5. Crie um repositório no github, faça commit e push para este repositório e entreque aqui apenas o 
# link do repositório.

cat1 = Categoria()
cat2 = Categoria("Dell")

d1 = Desktop("Gaming", "Preto", 2000, cat2.nome, 400)
d1.setPotencialDeBateria(1000)
d1.getInformacoes()

n1 = Notebook("HP", "Branca", 1500, cat1.nome, 7)
n1.getInformacoes()