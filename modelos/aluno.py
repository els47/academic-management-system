# Informações básicas do aluno
class Aluno:
    def __init__(self, matricula, nome, curso): # Novo objeto aluno
        self.matricula = matricula # Armazena a matrícula
        self.nome = nome # Armazena o nome 
        self.curso = curso # Armazena o curso 
    
    def __str__(self): # Mostra o texto
        return (f'Aluno {self.matricula} | {self.nome} | {self.curso}')