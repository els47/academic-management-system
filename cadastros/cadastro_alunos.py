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
        
        else:
            # Passo 2: Se o curso existe, vê se o aluno já ta nele
            ja_matriculado = False
            for a in alunos:
                # Confere se a matricula bate E se o curso é o mesmo
                if a.matricula == matricula and a.curso == nome_curso:
                    ja_matriculado = True
                    break

            if ja_matriculado:
                print(f"Erro: O aluno {matricula} já está matriculado neste curso.")
            else:
                # Tudo certo, cadastra
                novo_aluno = Aluno(matricula, nome, nome_curso)
                alunos.append(novo_aluno)
                print("Aluno cadastrado com sucesso!")

        continuar = input("\nDeseja cadastrar outro aluno? [S/N]: ").strip().upper()
        if continuar != 'S': # Se digitar qualquer coisa que não seja S, ele para
            break

    # Mostra a lista no final
    if alunos:
        print('-'*50)
        print('ALUNOS CADASTRADOS'.center(50))
        print('-'*50)
        for i, aluno in enumerate(alunos):
            print(f"{i + 1}. Matrícula: {aluno.matricula} | Nome: {aluno.nome} | Curso: {aluno.curso}")
        print('-'*50)
def deseja_continuar():
    while True:
        resp = input("Deseja cadastrar outro aluno? [S/N]: ").strip().upper()
    if resp in ['S', 'N']:
        return resp == 'S'
        print("Opção inválida. Digite S ou N.")