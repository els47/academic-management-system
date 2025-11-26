from cadastros.cadastro_cursos import cadastrar_cursos

def menu_cadastros(dados_sistema): # Utiliza como parâmetro os dados que estão armazenado globalmente
    while (True):
        print('-'*32)
        print('MENU DE CADASTRO'.center(32))
        print('-'*32)
        print('1 - Cadastrar curso')
        print('2 - Cadastrar disciplina')
        print('3 - Cadastrar professor')
        print('4 - Cadastrar aluno')
        print('5 - Cadastrar nota')
        print(''' ''')

        opc = int(input('Digite a sua opção: '))

        if opc == 1:
            cadastrar_cursos(dados_sistema['cursos'])
            break
        elif opc == 2:
            print("Cadastrar disciplina - Em desenvolvimento")
        elif opc == 3:
            print("Cadastrar professor - Em desenvolvimento")
        elif opc == 4:
            print("Cadastrar aluno - Em desenvolvimento")
        elif opc == 5:
            print("Cadastrar notas - Em desenvolvimento")
        elif opc == 6:
            print("Encerrando o sistema.")
        else:
            print("Opção inválida! Tente novamente.")

# menu_cadastros() 