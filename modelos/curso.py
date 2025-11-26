# Criando um classe que encapsula as informações básicas de um curso
class Curso:
    def __init__(self, codigo, nome): # Inicializa um novo objeto curso
        self.codigo = codigo # Armazena o código no atributo do objeto
        self.nome = nome # Armazena o nome no atributo do objeto
    
    def __str__(self): # Tornar legível para o usuário
        return (f'Curso {self.codigo}: {self.nome}')
    
    def __repr__(self):
        return (f"Curso(codigo='{self.codigo}', nome='{self.nome}'")