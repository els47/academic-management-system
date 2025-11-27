from modelos.aluno import Aluno

def cadastrar_alunos(alunos, cursos):
    while True:
        print("\n--- NOVO CADASTRO DE ALUNO ---")
        
        # Tenta pegar um numero, se digitar letra avisa o erro
        try:
            matricula = int(input("Matrícula: "))
        except ValueError:
            print("A matrícula precisa ser um número.")
            continue

        nome = str(input("Nome Completo: ")).strip().upper()
        # Mudei o nome da variavel aqui para nao confundir com a lista
        nome_curso = str(input("Nome do Curso: ")).strip().upper()

        # Passo 1: Verifica se o curso existe mesmo
        curso_existe = False
        for c in cursos:
            if c.nome == nome_curso:
                curso_existe = True
                break 
        
        if not curso_existe:
            print(f"Erro: O curso '{nome_curso}' não foi encontrado. Cadastre o curso primeiro.")
            if deseja_sair(): # Coloquei a função novamente para NÃO retornar ao cadastro de alunos automaticamente e ocasionar um loop infinito
                break # Volta para o menu de cadastro
            else:
                if not deseja_continuar(): # Coloquei a função novamente porque é ideal que o usuário digite S / N
                    break # Volta para o menu de cadastro
                else:
                    continue # Volta ao início do loop/ ao cadastro de alunos automaticamente
        
        else:
            # Passo 2: Se o curso existe, vê se o aluno já ta nele
            ja_matriculado = False
            for a in alunos:
                # Confere se a matricula bate E se o curso é o mesmo
                if a.matricula == matricula and a.curso == nome_curso:
                    ja_matriculado = True
                    break

            if ja_matriculado:
                print(f"Erro: O aluno {nome} já está matriculado neste curso.")
                if not deseja_continuar(): # Coloquei a função novamente para NÃO retornar ao cadastro de aluno automaticamente e ficar em um loop infinito
                    break
            else:
                # Tudo certo, cadastra
                novo_aluno = Aluno(matricula, nome, nome_curso)
                alunos.append(novo_aluno)
                print(f"Aluno(a) '{nome}' cadastrado(a) com sucesso!")

            if not deseja_continuar(): # Coloquei a função novamente porque é ideal que o usuário digite S / N
                break

    # Mostra a lista no final
    if alunos:
        print('-'*50)
        print('ALUNOS CADASTRADOS'.center(50))
        print('-'*50)
        for a in alunos:
            print(f"Matrícula: {a.matricula} | Nome: {a.nome} | Curso: {a.curso}")
        print('-'*50)


# Função para verificar se o usuário deseja continuar
def deseja_continuar():
    while True:
        resp = input("Deseja cadastrar outro(a) aluno(a)? [S/N]: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['S', 'N']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")

# Função para verificar se o usuário deseja retornar ao menu de cadastro quando um curso não for encontrado ou um aluno já estiver cadastrado
def deseja_sair():
    while True:
        resp = input("Deseja retornar ao Menu de Cadastro? [S/N]: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['S', 'N']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")