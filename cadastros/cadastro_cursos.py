from modelos.curso import Curso

def cadastrar_curso(cursos):
    while True:
        print("\n--- CADASTRO DE CURSO ---")
        
        # Tirei o 'int' para aceitar letras (ex: 'CC', 'SI')
        codigo = input("Código (ex: CC): ").strip().upper()
        
        # Verifica logo se o código já existe
        existe_codigo = any(c.codigo == codigo for c in cursos)
        
        if existe_codigo:
            print(f"Erro: Já existe um curso com o código '{codigo}'. Tente outro.")
            continue # Volta para o começo sem pedir o nome

        # Só pede o nome se o código for livre
        nome = input("Nome do Curso: ").strip().upper()
        
        novo_curso = Curso(codigo, nome)
        cursos.append(novo_curso)
        print(f"Curso '{nome}' cadastrado com sucesso!")

        # Simplifiquei a pergunta
        if not deseja_continuar(): # Coloquei a função novamente porque é ideal que o usuário digite S / N
            break

    if cursos:
        print('-'*40)
        print('CURSOS CADASTRADOS'.center(40))
        print('-'*40)
        for c in cursos:
            print(f"[{c.codigo}] - {c.nome}")
        print('-'*40)


# Função para verificar se o usuário deseja continuar
def deseja_continuar():
    while True:
        resp = input("Deseja cadastrar outro curso? [S/N]: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['S', 'N']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")