# Chamando a classe Curso
from modelos.aluno import Aluno

#TODO: PESQUISAR COMO A FUNÇÃO RECEBE ESSAS LISTAS SE NÃO TÊM IMPORT DO MAIN PARA ESSE ARQUIVO
def cadastrar_alunos(alunos, cursos): # Utiliza como parâmetros os dados globais com a lista de alunos. Faz a conexão com a de cursos
    while(True):

        # Recebendo valores do usuário
        matricula = int(input("Matrícula: "))
        nome = str(input("Nome Completo: ")).strip().upper()
        curso = str(input("Curso: ")).strip().upper()

        #TODO: O cadastro de um aluno só é realizado se houver o curso cadastrado nos dados globais. Depois, verifica-se se já existe matrícula no curso em específico, para evitar duplicidade
        existeMatricula = any(c.matricula == matricula for c in alunos) # Acessa o atributo matricula ao percorrer cada aluno da lista

        for indice, curso in enumerate(cursos): # Acessa o índice e o valor de cada item da lista
            if curso.nome in alunos['curso']: #TODO: COMO VERIFICAR SE O ALUNO ESTÁ NO CURSO CADASTRADO EM ESPECÍFICO? 
                print("Volte ao menu de cadastro para realizar o cadastro do curso!")
            else:
                if existeMatricula and curso.nome: #TODO: COMO VERIFICAR SE A MATRÍCULA JÁ ESTÁ CADASTRADO NESSE CURSO?
                    print(f'Aluno já cadastrado no curso "{curso.nome}". Tente novamente!')
                else:
                    # Cria um objeto da classe Curso
                    novo_aluno = Aluno(matricula, nome, curso)

                    # Adiciona o objeto à lista
                    alunos.append(novo_aluno) 
                    print(f"Aluno cadastrado!")
            
        # Confirmação de continuidade ou não  
        if not deseja_continuar():
            break

    if alunos: # Se houver alunos na lista, exibirá isso:
        print('-'*50)
        print('ALUNOS CADASTRADOS'.center(50))
        print('-'*50)
        print(''' ''')
        for indice, aluno in enumerate(alunos): # Acessa atributos do objeto
            print(f"{indice}.Matrícula: {aluno.matricula} | Nome: {aluno.nome} | Curso: {aluno.curso}") # Acessar atributos do objeto
        print(''' ''')
    else: # Se não houver alunos, exibirá isso:
        print('/'*50)
        print('ATENÇÃO!!!'.center(50))
        print('/'*50)
        print('ALUNO NÃO CADASTRADO. VERIFIQUE SE HÁ O CURSO NO SISTEMA"')
        print(''' ''')

def deseja_continuar():
    while True:
        r = input("Deseja cadastrar outro aluno? [S/N]: ").strip().upper()[0]
        if r in ['S', 'N']: # Aceita apenas essas duas letras
            return r == 'S'   # True continua, False para. Está dentro da função de cadastro.