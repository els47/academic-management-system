from modelos.aluno import Aluno

def cadastrar_alunos(alunos, cursos):
    while True:
        print("\n--- NOVO CADASTRO DE ALUNO ---")
        
        # Matrícula
        try:
            matricula = int(input("Matrícula: "))
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
            nome = aluno_existente.nome
        
        # 2-Se é matrícula nova - Pede o nome e valida
        else:
            nome = str(input("Nome Completo: ")).strip().upper()

            # Verifica se esse nome já existe em outra matrícula
            nome_tem_outra_matricula = False
            for a in alunos:
                if a.nome == nome:
                    print(f"Erro: O aluno '{nome}' já possui cadastro com a matrícula {a.matricula}.")
                    nome_tem_outra_matricula = True
                    break
            
            # Se der erro de identidade:
            if nome_tem_outra_matricula:
                if not deseja_tentar_novamente():
                    break # Sai do cadastro
                else:
                    continue # Volta para pedir a matrícula de novo

        # Curso
        nome_curso = str(input("Nome do Curso: ")).strip().upper()

        # Valida se o curso existe
        curso_existe = False
        for c in cursos:
            if c.nome == nome_curso:
                curso_existe = True
                break 
        
        if not curso_existe:
            print(f"Erro: O curso '{nome_curso}' não foi encontrado. Cadastre o curso primeiro.")
        
        else:
            # Validação dupla
            # O aluno (matrícula + nome) já tá nesse curso?
            ja_matriculado = False
            for a in alunos:
                if a.matricula == matricula and a.curso == nome_curso:
                    ja_matriculado = True
                    break

            if ja_matriculado:
                print(f"Erro: O aluno '{nome}' já está matriculado no curso de {nome_curso}.")
            else:
                novo_aluno = Aluno(matricula, nome, nome_curso)
                alunos.append(novo_aluno)
                print(f"Sucesso: Aluno(a) '{nome}' matriculado(a) em {nome_curso}!")

        # Aqui tava tendo erro de repetição
        if not deseja_continuar():
            break

    # Mostra a lista no final
    if alunos:
        print('-'*50)
        print('ALUNOS CADASTRADOS'.center(50))
        print('-'*50)
        for i, aluno in enumerate(alunos):
            print(f"{i + 1}. Matrícula: {aluno.matricula} | Nome: {aluno.nome} | Curso: {aluno.curso}")
        print('-'*50)


# Função para verificar se o usuário deseja continuar
def deseja_continuar():
    while True:
        resp = input("\nDeseja cadastrar outro(a) aluno(a)? [S/N]: ").strip().upper()
        if resp in ['S', 'N']:
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")

# Função para verificar se o usuário deseja retornar ao menu de cadastro quando um curso não for encontrado ou um aluno já estiver cadastrado
def deseja_tentar_novamente():
    while True:
        resp = input("\nDeseja tentar novamente? [S/N]: ").strip().upper()
        if resp in ['S', 'N']:
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")