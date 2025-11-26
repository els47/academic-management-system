# def cadastrar_professores (professores)
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
            # Volta para o início do loop sem cadastrar
            continue 

        # Confirmando se a disciplina existe
        nome_disciplina = input("Nome da Disciplina: ").strip().upper()
        
        disciplina_encontrada = False
        for d in disciplinas:
            if d.nome == nome_disciplina: 
                disciplina_encontrada = True
                break
        
        if not disciplina_encontrada:
            print(f"ERRO: A disciplina '{nome_disciplina}' não existe! Cadastre-a primeiro.")
            continue

        # Se ok, cadastra!
        novo_prof = Professor(matricula, nome, nome_disciplina, nome_curso)
        professores.append(novo_prof)
        print("Professor cadastrado com sucesso!")

        if input("Continuar? [S/N]: ").upper() != 'S':
            break