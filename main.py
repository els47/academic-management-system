               
from menu.menu_cadastro import menu_cadastros
from menu.menu_status import exibir_status_geral
from menu.menu_certificado import gerar_certificado
from relatorios.relatorio_geral import exibir_relatorio_geral
from relatorios.relatorio_matriculas import menu_relatorio_matriculas
from relatorios.relatorio_boletim import exibir_boletim_individual


def main():
    # Armazena dados temporariamente na memória RAM
    dados_sistema = {
        'cursos': [],
        'disciplinas': [],
        'professores': [],
        'alunos': [],
        'notas': [],
    }
  
    while True:
        print('-'*32)
        print('SISTEMA DE GESTÃO ACADÊMICA'.center(32))
        print('-'*32)
        print('1 - Menu de Cadastros')
        print('2 - Status do Aluno (Notas & CR)') # Conectado ao exibir_status_geral
        print('3 - Emitir Certificado')          # Conectado ao gerar_certificado
        print('4 - Relatório Geral')
        print('5 - Relatório Matrículas')
        print('6 - Relatório do Aluno')
        print('7 - Sair')
        print(''' ''')
        
        try:
            opc = int(input('Digite a sua opção: '))
        except ValueError:
            print("Por favor, digite um número.")
            continue

        print(''' ''')
        
        if opc == 1:
            menu_cadastros(dados_sistema) 
        
        elif opc == 2:
            # Calcula a média geral e recuperação
            exibir_status_geral(dados_sistema['alunos'], dados_sistema['notas'])
            
        elif opc == 3:
            # Verificar aprovação e gerar certificado
            gerar_certificado(dados_sistema['alunos'], dados_sistema['notas'])
        
        elif opc == 4:
            exibir_relatorio_geral(dados_sistema['alunos'], dados_sistema['cursos'], dados_sistema['disciplinas'], dados_sistema['professores'])
            
        elif opc == 5: # relatorio de turmas
            menu_relatorio_matriculas(dados_sistema['alunos'], dados_sistema['cursos'], dados_sistema['disciplinas'], dados_sistema['notas'])

        elif opc == 6: # visualiza boletim individual
            exibir_boletim_individual(dados_sistema['alunos'], dados_sistema['notas'])

        elif opc == 7:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()