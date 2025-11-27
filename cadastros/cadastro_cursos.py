from modelos.curso import Curso

def cadastrar_curso(cursos):
    while True:
        print("\n--- CADASTRO DE CURSO ---")
        
        # Tirei o 'int' para aceitar letras (ex: 'CC', 'SI')
        codigo = input("Código (ex: CC): ").strip().upper()
        
        # Verifica se o código já existe na lista
        existe_codigo = False
        for c in cursos:
            if c.codigo == codigo:
                existe_codigo = True
                break

        if existe_codigo:
            print(f"Erro: Já existe um curso com o código '{codigo}'. Cadastre outro.")
            if deseja_sair(): # Coloquei a função novamente para NÃO retornar ao cadastro de cursos automaticamente e ocasionar um loop infinito
                break 
            else:
                if not deseja_continuar(): # Coloquei a função novamente porque é ideal que o usuário digite S / N
                    break # Volta para o Menu de Cadastro
                else:
                    continue # Volta para o loop inicial/cadastro de disciplinas automaticamente

        else:
            # Só pede o nome se o código for livre
            nome = input("Nome do Curso: ").strip().upper()
            
            novo_curso = Curso(codigo, nome)
            cursos.append(novo_curso)
            print(f"Curso '{nome}' cadastrado com sucesso!")

            # Coloquei a função novamente porque é ideal que o usuário digite S / N
            if not deseja_continuar(): 
                break

    if cursos:
        print('-'*40)
        print('CURSOS CADASTRADOS'.center(40))
        print('-'*40)
        for c in cursos:
            print(f"Código: [{c.codigo}] - Nome: {c.nome}")
        print('-'*40)


# Função para verificar se o usuário deseja continuar
def deseja_continuar():
    while True:
        resp = input("Deseja cadastrar outro curso? [S/N]: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['S', 'N']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")

# Função para verificar se o usuário deseja retornar ao menu de cadastro quando um código já estiver cadastrado
def deseja_sair():
    while True:
        resp = input("Deseja retornar ao Menu de Cadastro? [S/N]: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['S', 'N']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")