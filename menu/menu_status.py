from status.status_alunos import calcular_media

def menu_status(dados_sistema):

    while True:
        print('-'*32)
        print('Menu de Status'.center(32))
        print('-'*32)
        print('1 - Verificar Status do Aluno')
        print('2 - Emitir Certificado')
        print('3 - Voltar ao Menu Principal')
        print(''' ''')

        opc = int(input('Digite a sua opção: '))

        print(''' ''')

        if opc == 1:
            calcular_media(
                dados_sistema['alunos'],
                dados_sistema['cursos'],
                dados_sistema['disciplinas'],
                dados_sistema['notas'])
        #elif opc == 2:
         #   emitir_certificado()
        elif opc == 3:
            break
        else:
            print("Opção inválida! Tente novamente.")