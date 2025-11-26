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
        print(f"Sucesso: Curso '{nome}' cadastrado!")

        # Simplifiquei a pergunta
        if input("\nCadastrar outro curso? [S/N]: ").strip().upper() != 'S':
            break

    if cursos:
        print('-'*40)
        print('CURSOS ATUAIS')
        for c in cursos:
            print(f"[{c.codigo}] - {c.nome}")
        print('-'*40)