from cadastros.cadastro_cursos import cadastrar_curso
from cadastros.cadastro_alunos import cadastrar_alunos
from cadastros.cadastro_disciplinas import cadastrar_disciplina
from cadastros.cadastro_professores import cadastrar_professor
from cadastros.cadastro_notas import cadastrar_notas
from modelos.aluno import Aluno

def menu_cadastros(dados_sistema): # Utiliza como parâmetro os dados que estão armazenado globalmente
    while (True):
        print('-'*32)
        print('Menu de Cadastro'.center(32))
        print('-'*32)
        print('1 - Curso')
        print('2 - Disciplina')
        print('3 - Professor')
        print('4 - Aluno')
        print('5 - Nota')
        print('6 - Voltar ao Menu Principal')
        print(''' ''')

        opc = int(input('Digite a sua opção: '))
        print(''' ''')

        if opc == 1:
            cadastrar_curso(dados_sistema['cursos'])
        elif opc == 2:
            cadastrar_disciplina(dados_sistema['disciplinas'])
        elif opc == 3:
            cadastrar_professor(
                dados_sistema['professores'], 
                dados_sistema['cursos'], 
                dados_sistema['disciplinas'])
        elif opc == 4:
            cadastrar_alunos(
                dados_sistema['alunos'], 
                dados_sistema['cursos'])
        elif opc == 5:
            cadastrar_notas(
                dados_sistema['notas'],
                dados_sistema['alunos'],
                dados_sistema['disciplinas'])
        elif opc == 6:
            break
        else:
            print("Opção inválida! Tente novamente.")
