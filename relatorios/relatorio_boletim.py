# Vai mostrar os boletins individuais

def exibir_boletim_individual(alunos, notas):
    print("\n --- BOLETIM INDIVIDUAL DO ALUNO ---")
    matricula = input("Digite a matrícula do aluno: ").strip()

    aluno_encontrado = None
    for a in alunos:
        if str(a.matricula) == matricula:
            aluno_encontrado = a
            break

    if not aluno_encontrado:
        print("=== ERRO: Aluno não encontrado. ===")
        input("Pressione ENTER para voltar...")
        return
    
    print("="*50)
    print(f"ALUNO: {aluno_encontrado.nome}")
    print(f"CURSO: {aluno_encontrado.curso}")
    print(f"MATRÍCULA: {aluno_encontrado.matricula}")
    print("="*50)
    print(f"{'DISCIPLINA':<25} | {'NOTA':<5} | {'SITUAÇÃO'}")
    print("-" * 50)

    #Exibir notas
    notas_aluno = []
    for n in notas:
        if n.aluno == aluno_encontrado.nome:
            notas_aluno.append(n)

    if not notas_aluno:
        print(" (Nenhuma disciplina cursada) ")
    else:
        soma = 0.0
        for n in notas_aluno:
            # Visualizar status
            if n.nota >= 7.0:
                status = "ESTÁ APROVADO!"
            elif n.nota >= 4.0:
                status = "EM RECUPERAÇÃO."
            else:
                status = "REPROVADO."

            nome_disc = getattr(n.disciplina, 'nome', str(n.disciplina))

            print(f"{nome_disc:<25} | {n.nota:.1f} | {status}")
            soma += n.nota

        # Cálculo do CR
        media_geral = soma / len(notas_aluno)
        print("-" * 50)
        print(f"MÉDIA GERAL DO CURSO (CR): {media_geral:.2f}")

    print("="*50)
    input("\n Pressione ENTER para fechar a janela do boletim.")
    