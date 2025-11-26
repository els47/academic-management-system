from menu.menu_cadastro import menu_cadastros

# from menu.menu_relatorio import menu_relatorios
# from menu.menu_certificado import menu_certificados

def main():
    # Armazena dados temporariamente
    dados_sistema = {
        'cursos': [],
        'disciplinas': [],
        'professores': [],
        'alunos': [],
        'notas': []
    }
    
    while True:
        print('-'*32)
        print('MENU PRINCIPAL'.center(32))
        print('-'*32)
        print('1 - Menu de Cadastros')
        print('2 - Menu de Relatórios')
        print('3 - Menu de Certificados')
        print('4 - Sair')
        print(''' ''')
        
        opc = int(input('Digite a sua opção: '))
        print(''' ''')
        
        if opc == 1:
            menu_cadastros(dados_sistema)  # Passa os dados 
        #elif opc == 2:
         #   menu_relatorios(dados_sistema)
         #elif opc == 3:
         #  menu_certificados() # Qual será o parâmetro global?
        elif opc == 4:
            break
        else:
            print("Opção inválida! Tente novamente.")

#TODO: PESQUISAR A FUNÇÃO DESSE BLOCO DE CÓDIGO
if __name__ == "__main__":
    main()