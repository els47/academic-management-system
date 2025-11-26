# Chamando a classe Curso
from modelos.curso import Curso

def cadastrar_cursos(cursos): # Cadastro dos cursos utilizando a classe Curso
    while(True):

        # Recebendo valores do usuário
        codigo = int(input("Código: "))
        nome = str(input("Nome: ")).strip().upper()

        # Validando se os dados já existem. Objetos são acessados com ponto, diferente de dicionários
        existeCodigo = any(c.codigo == codigo for c in cursos) 
        existeNome = any(c.nome == nome for c in cursos)

        if existeCodigo or existeNome:
            print("Curso já cadastrado. Tente novamente!")
        else:
            # Cria um objeto da classe Curso
            novo_curso = Curso(codigo, nome)

            # Adiciona o objeto à lista
            cursos.append(novo_curso) 
            print(f"Curso cadastrado!")
            
        # Confirmação de continuidade ou não  
        if not deseja_continuar():
            break
        
    # Iteração dos pares chave:valor e exibição para o usuário
    print('-'*50)
    print('CURSOS CADASTRADOS'.center(50))
    print('-'*50)
    print(''' ''')

    if cursos:
        for indice, curso in enumerate(cursos, 1): # Acessa atributos do objeto
            print(f"{indice}. Código: {curso.codigo} | Nome: {curso.nome}") # Acessar os atributos do objeto
        print(''' ''')
    else:
        print('Nenhum curso cadastrado!')

def deseja_continuar():
    while True:
        r = input("Deseja cadastrar outro curso? [S/N]: ").strip().upper()[0]
        if r in ['S', 'N']:
            return r == 'S'   # True continua, False para. Está dentro da função de cadastro.

