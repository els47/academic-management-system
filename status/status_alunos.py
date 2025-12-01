from modelos.nota import Nota

def calcular_media(alunos, cursos, disciplinas, notas):
    while True:
        # Solicitar a matrícula
        try:
            matricula = input("Matrícula: ")
        except ValueError:
            print("A matrícula precisa ser um número.")
            continue

        # Nome
        aluno_existente = None
        for a in alunos:
            if a.matricula == matricula:
                aluno_existente = a
                break
        
        # 1-Se a matrícula já existe no sistema - Puxa o nome
        if aluno_existente:
            print(f" >> Matrícula encontrada! Pertence ao aluno: {aluno_existente.nome}")

        
        # 2-Se o aluno não estiver cadastrado, impede a continuação do laço
        else:
            print(f'=== ERRO: A matrícula {matricula} não foi encontrada. Cadastre-a primeiro! ===')
            if deseja_sair(): # Coloquei a função novamente para NÃO retornar ao cadastro de disciplinas automaticamente e ocasionar um loop infinito
                break 
            else:
                if not deseja_continuar(): # Coloquei a função novamente porque é ideal que o usuário digite S / N
                    break # Volta para o Menu de Status
                else:
                    continue # Volta para o loop inicial/verificação de status automaticamente

#TODO: PASSO A PASSO
#TODO: 1) Pegar a matrícula para fazer a verificação 2) Pegar o curso que o aluno está fazendo 3) Receber todas as disciplinas e respectivas notas cadastradas no curso para retirar a média


# Função para verificar se o usuário deseja continuar
def deseja_continuar():
    while True:
        resp = input("\nDeseja verificar outro(a) aluno(a)? [S/N]: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['S', 'N']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")

# Função para verificar se o usuário deseja retornar ao menu de status quando a matrícula ou a disciplina não forem encontrados
def deseja_sair():
    while True:
        resp = input("\nDeseja retornar ao Menu de Status? [S/N]: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['S', 'N']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")