class Aluno:
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        texto = "Codigo: " + str(self.codigo)
        texto += "\nNome: " + self.nome
        texto += "\nMatricula: " + self.matricula
        return texto

    def imprimir(self):
        print( self )
        
    
class AlunoEnsinoMedio(Aluno):
    def __init__(self, codigo, nome, matricula, ano = 2023):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano
        
    def __str__(self):
        # texto = "Codigo: " + str(self.codigo)
        # texto += "Nome: " + self.nome
        # texto += "Matricula: " + self.matricula
        texto = super().__str__()
        texto += "Ano: " + str(self.ano)
        return texto
        
    def imprimir(self):
        # super().imprimir() 
        # print( "Ano: " + str(self.ano))
        print(self)

class AlunoGraduacao(Aluno):
    def __init__(self, codigo, nome, matricula, semestre = 3):
        Aluno.__init__(self, codigo, nome, matricula)
        self.semestre = semestre
        
    def __str__(self):
        texto = "Codigo: " + str(self.codigo)
        texto += "\nNome: " + self.nome
        texto += "\nMatricula: " + self.matricula
        texto += "\nSemestre: " + str(self.semestre)
        return texto
        
    def imprimir(self):
        # Aluno.imprimir() 
        print(self)