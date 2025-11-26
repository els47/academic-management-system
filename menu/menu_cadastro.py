from cadastros.cadastro_cursos import cadastrar_cursos
from cadastros.cadastro_alunos import cadastrar_alunos

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
            cadastrar_cursos(dados_sistema['cursos'])
        elif opc == 2:
            print("Cadastrar disciplina - Em desenvolvimento")
        elif opc == 3:
            print("Cadastrar professor - Em desenvolvimento")
        elif opc == 4:
            cadastrar_alunos(dados_sistema['alunos'], dados_sistema['cursos'])
        elif opc == 5:
            print("Cadastrar notas - Em desenvolvimento")
        elif opc == 6:
            break
        else:
            print("Opção inválida! Tente novamente.")
