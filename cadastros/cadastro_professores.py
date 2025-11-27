from modelos.professor import Professor

def cadastrar_professor(professores, cursos, disciplinas):
    while True:
        print("\n--- CADASTRO DE PROFESSOR ---")
        
        matricula = input("Matrícula: ")
        nome = input("Nome do Professor: ").strip().upper()
        
        # Confirmando se o curso existe
        nome_curso = input("Nome do Curso que leciona: ").strip().upper()
        
        curso_encontrado = False
        for c in cursos:
            if c.nome == nome_curso:
                curso_encontrado = True
                break
        
        if not curso_encontrado:
            print(f"ERRO: O curso '{nome_curso}' não existe! Cadastre o curso primeiro.")
            if deseja_sair(): # Coloquei a função novamente para NÃO retornar ao cadastro de professores automaticamente e ocasionar um loop infinito
                break 
            else:
                if not deseja_continuar(): # Coloquei a função novamente porque é ideal que o usuário digite S / N
                    break # Volta para o Menu de Cadastro
                else:
                    continue # Volta para o loop inicial/cadastro dos professores automaticamente

        else: 
            # Se o curso existe, precisamos confirmar se a disciplina existe
            nome_disciplina = input("Nome da Disciplina: ").strip().upper()
            
            disciplina_encontrada = False
            for d in disciplinas:
                if d.nome == nome_disciplina: 
                    disciplina_encontrada = True
                    break
            
            if not disciplina_encontrada:
                print(f"ERRO: A disciplina '{nome_disciplina}' não existe! Cadastre-a primeiro.")
                if deseja_sair(): # Coloquei a função novamente para NÃO retornar ao cadastro de professores automaticamente e ocasionar um loop infinito
                    break 
                else:
                    if not deseja_continuar(): # Coloquei a função novamente porque é ideal que o usuário digite S / N
                        break # Volta para o Menu de Cadastro
                    else:
                        continue # Volta para o loop inicial/cadastro dos professores automaticamente

            # Se ok, cadastra!
            novo_prof = Professor(matricula, nome, nome_disciplina, nome_curso)
            professores.append(novo_prof)
            print(f"Professor(a) '{nome}' cadastrado(a) com sucesso!")

            if not deseja_continuar(): # Coloquei a função novamente porque é ideal que o usuário digite S / N
                    break
    
    # Mostra a lista no final
    if professores:
        print('-'*50)
        print('PROFESSORES CADASTRADOS'.center(50))
        print('-'*50)
        for p in professores:
            print(f"Matrícula: {p.matricula} | Nome: {p.nome} | Curso: {p.curso} | Disciplina: {p.disciplina}")
        print('-'*50)


# Função para verificar se o usuário deseja continuar
def deseja_continuar():
    while True:
        resp = input("\nDeseja cadastrar outro(a) professor(a)? [S/N]: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['S', 'N']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")

# Função para verificar se o usuário deseja retornar ao menu de cadastro quando uma disciplina ou curso não for encontrado
def deseja_sair():
    while True:
        resp = input("\nDeseja retornar ao Menu de Cadastro? [S/N]: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['S', 'N']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")