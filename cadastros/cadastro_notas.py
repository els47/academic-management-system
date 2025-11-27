from modelos.nota import Nota

def cadastrar_notas(notas, alunos, disciplinas):
    while True:
        print("\n--- CADASTRO DE NOTAS ---")

        # Tenta pegar um numero, se digitar letra avisa o erro
        try:
            nota = int(input('Nota: '))
        except ValueError:
            print("A nota precisa ser um número.")
            continue

        nome_aluno = str(input("Nome Completo: ")).strip().upper()
        nome_disciplina = str(input("Nome da Disciplina: ")).strip().upper()

        #TODO Verifica se o aluno já existe

        #TODO Verifica se a disciplina existe

        #TODO Verifica se o aluno está cadastrado na disciplina

        #TODO Realizar o cadastro do aluno 

        #TODO Exibir opção de continuar

        #TODO Exibir lista final com aluno - disciplina - nota