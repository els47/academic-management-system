from modelos.nota import Nota

def cadastrar_notas(notas, alunos, disciplinas):
    while True:
        print("\n--- CADASTRO DE NOTAS ---")

        # Verificando se o aluno já está cadastrado
        nome_aluno = str(input("Nome Completo do Aluno(a): ")).strip().upper()

        aluno_existe = False
        for a in alunos:
            if a.nome == nome_aluno:
                aluno_existe = True
                break
        
        if not aluno_existe:
            print(f"Erro: O aluno(a) '{nome_aluno}' não foi encontrado(a). Cadastre-o(a) primeiro.")
            if deseja_sair(): # Coloquei a função novamente para NÃO retornar ao cadastro de notas automaticamente e ocasionar um loop infinito
                break 
            else:
                if not deseja_continuar(): # Coloquei a função novamente porque é ideal que o usuário digite S / N
                    break # Volta para o Menu de Cadastro
                else:
                    continue # Volta para o loop inicial/cadastro de notas automaticamente
        else:

            # Se o aluno existe, é preciso verificar se a disciplina existe.
            codigo_disciplina = str(input("Código da Disciplina: ")).strip().upper()

            # Utilizar o código que é um identificador único e, com isso, evitar duplicidades de notas
            disciplina_existe = False
            for d in disciplinas:
                if d.codigo == codigo_disciplina:
                    disciplina_existe = True
                    break
            
            if not disciplina_existe:
                print(f"ERRO: A disciplina '{codigo_disciplina}' não existe! Cadastre-a primeiro.")
                if deseja_sair(): # Coloquei a função novamente para NÃO retornar ao cadastro de notas automaticamente e ocasionar um loop infinito
                    break 
                else:
                    if not deseja_continuar(): # Coloquei a função novamente porque é ideal que o usuário digite S / N
                        break # Volta para o Menu de Cadastro
                    else:
                        continue # Volta para o loop inicial/cadastro de notas automaticamente
            
            # Se ambos existem, então posso atribuir uma nota
            else:
                nota = str(input("Nota: "))

                nova_nota = Nota(nome_aluno, codigo_disciplina, nota)
                notas.append(nova_nota)
                print(f"Nota '{nota}' cadastrada com sucesso!")

            # Coloquei a função novamente porque é ideal que o usuário digite S / N
            if not deseja_continuar(): 
                break

    if notas:
        print('-'*50)
        print('NOTAS CADASTRADAS'.center(50))
        print('-'*50)
        for n in notas:
            print(f"Aluno: {n.aluno} | Disciplina:[{n.disciplina}] | Nota{n.nota}")
        print('-'*50)


# Função para verificar se o usuário deseja continuar
def deseja_continuar():
    while True:
        resp = input("\nDeseja cadastrar outra nota? [S/N]: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['S', 'N']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")

# Função para verificar se o usuário deseja retornar ao menu de cadastro quando um aluno ou disciplina não estiver cadastrado
def deseja_sair():
    while True:
        resp = input("\nDeseja retornar ao Menu de Cadastro? [S/N]: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['S', 'N']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")