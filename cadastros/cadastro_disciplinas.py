from modelos.disciplina import Disciplina

def cadastrar_disciplina(disciplinas):
    while True:
        print("\n--- CADASTRO DE DISCIPLINA ---")
        
        # Pede os dados e transforma em Maiúsculo
        codigo = str(input("Código (ex: COMP1): ")).strip().upper()
        nome = str(input("Nome da Disciplina: ")).strip().upper()

        # Verifica se já existe esse código na lista
        ja_existe = False
        for d in disciplinas:
            if d.codigo == codigo:
                ja_existe = True
                break
        
        if ja_existe:
            print(f"ERRO: O código '{codigo}' já está cadastrado!")
        else:
            # Cria a disciplina nova e salva na lista
            nova_disciplina = Disciplina(codigo, nome)
            disciplinas.append(nova_disciplina)
            print(f"Sucesso: Disciplina '{nome}' cadastrada!")

        # Pergunta se quer continuar
        continuar = input("\nCadastrar outra? [S/N]: ").strip().upper()
        if continuar != 'S':
            break