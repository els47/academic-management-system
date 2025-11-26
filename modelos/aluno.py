# Criando um classe que encapsula as informações básicas de um aluno
class Aluno:
    def __init__(self, matricula, nome, curso): # Inicializa um novo objeto aluno
        self.matricula = matricula # Armazena a matrícula no atributo do objeto
        self.nome = nome # Armazena o nome no atributo do objeto
        self.curso = curso # Armazena o curso no atributo do objeto
    
    def __str__(self): # Tornar legível para o usuário
        return (f'Aluno {self.matricula} | {self.nome} | {self.curso}')