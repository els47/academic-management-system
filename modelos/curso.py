# Informações de um curso
class Curso:
    def __init__(self, codigo, nome): # Novo objeto curso
        self.codigo = codigo # Armazena o código
        self.nome = nome # Armazena o nome 
    
    def __str__(self): # Mostra o texto
        return (f'Curso {self.codigo} | {self.nome}')