from pilha import Pilha
from livro import Livro

pilha = Pilha()

# livro1 = Livro("The Hobbit", "J.R.R. Tolkien", 250)
# livro2 = Livro("A song of fire and ice", "George R.R. Martin", 547)
# livro3 = Livro("1984", "George Orwell", 314)

pilha.add("The Hobbit", "J.R.R. Tolkien", 250)
pilha.add("A song of fire and ice", "George R.R. Martin", 547)
pilha.add("1984", "George Orwell", 314)

pilha.remover()

pilha.imprimir()