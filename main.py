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
            
        elif opc == 2:
            print(f"Cursos cadastrados: {len(dados_sistema['cursos'])}") # Exibe os dados armazenados
            
        elif opc == 4:
            break

if __name__ == "__main__":
    main()