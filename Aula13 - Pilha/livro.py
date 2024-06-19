class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.proximo = None
        
    def __str__(self):
        return f"{self.titulo} {self.autor} {self.paginas}"