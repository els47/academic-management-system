from modelos.disciplina import Disciplina

def cadastrar_disciplina(cursos, disciplinas):
    while True:
        print("\n--- CADASTRO DE DISCIPLINA ---")

        # Verifica se existe o curso cadastrado
        nome_curso = str(input("Nome do Curso: ")).strip().upper()

        curso_existe = False
        for c in cursos:
            if c.nome == nome_curso:
                curso_existe = True
                break
        
        if not curso_existe:
            print(f"=== ERRO: Curso '{nome_curso}' não encontrado. Cadastre o curso primeiro! ===")
            if deseja_sair(): # Coloquei a função novamente para NÃO retornar ao cadastro de disciplinas automaticamente e ocasionar um loop infinito
                break 
            else:
                if not deseja_continuar(): # Coloquei a função novamente porque é ideal que o usuário digite S / N
                    break # Volta para o Menu de Cadastro
                else:
                    continue # Volta para o loop inicial/cadastro de disciplinas automaticamente
        else:
            # Pede os dados e adiciona um entrada inicial para evitar coincidência com os nomes dos cursos
            codigo = str(input("Código da Disciplina: COMP")).strip().upper()

            # Verifica se já existe esse código na lista
            ja_existe = False
            for d in disciplinas:
                if d.codigo == codigo:
                    ja_existe = True
                    break

            if ja_existe:
                print(f"=== ERRO: O código '[COMP{codigo}]' já está cadastrado! ===")
                if deseja_sair(): # Coloquei a função novamente para NÃO retornar ao cadastro de disciplinas automaticamente e ocasionar um loop infinito
                    break 
                else:
                    if not deseja_continuar(): # Coloquei a função novamente porque é ideal que o usuário digite S / N
                        break # Volta para o Menu de Cadastro
                    else:
                        continue # Volta para o loop inicial/cadastro de disciplinas automaticamente

            else:

                # Verificar se já existe disciplina com outro nome
                nome = str(input("Nome da Disciplina: ")).strip().upper()

                # Verifica se já existe esse nome na lista
                nome_existe = False
                for d in disciplinas:
                    if d.nome == nome:
                        nome_existe = True
                        break

                if nome_existe:
                    print(f"=== ERRO: O código '{nome}' já está cadastrado! ===")
                    if deseja_sair(): # Coloquei a função novamente para NÃO retornar ao cadastro de disciplinas automaticamente e ocasionar um loop infinito
                        break 
                    else:
                        if not deseja_continuar(): # Coloquei a função novamente porque é ideal que o usuário digite S / N
                            break # Volta para o Menu de Cadastro
                        else:
                            continue # Volta para o loop inicial/cadastro de disciplinas automaticamente
                else:
                    # Cria a disciplina nova e salva na lista
                    nova_disciplina = Disciplina(nome_curso, codigo, nome)
                    disciplinas.append(nova_disciplina)
                    print(f"Disciplina '{nome}' cadastrada com sucesso!")

                    if not deseja_continuar(): # Coloquei a função novamente porque é ideal que o usuário digite S / N
                        break
    
    # Mostra a lista no final
    if disciplinas:
        print('-'*50)
        print('DISCIPLINAS CADASTRADAS'.center(50))
        print('-'*50)
        for d in disciplinas:
            print(f"Curso: {d.curso} | Código da Disciplina: [COMP{d.codigo}] | Nome: {d.nome}")
        print('-'*50)


# Função para verificar se o usuário deseja continuar
def deseja_continuar():
    while True:
        resp = input("\nDeseja cadastrar outra disciplina? [S/N]: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['S', 'N']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")

# Função para verificar se o usuário deseja retornar ao menu de cadastro quando um código não for encontrado
def deseja_sair():
    while True:
        resp = input("\nDeseja retornar ao Menu de Cadastro? [S/N]: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['S', 'N']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")