def exibir_status_geral(alunos, notas):
    print("\n--- STATUS ACADÊMICO (MÉDIA GLOBAL & RECUPERAÇÃO) ---")
    
    # Buscar aluno
    matricula = input("Digite a Matrícula do aluno: ").strip()
    
    aluno_encontrado = None
    for a in alunos:
        if str(a.matricula) == matricula:
            aluno_encontrado = a
            break
            
    if not aluno_encontrado:
        print("Erro: Aluno não encontrado.")
        return

    print(f"\n>> Aluno: {aluno_encontrado.nome} | Curso: {aluno_encontrado.curso}")

    # Filtrar notas aluno
    notas_do_aluno = {} 

    for n in notas:
        if n.aluno == aluno_encontrado.nome:
            if n.disciplina not in notas_do_aluno or n.nota > notas_do_aluno[n.disciplina].nota:
                notas_do_aluno[n.disciplina] = n

    if not notas_do_aluno:
        print("Nenhuma disciplina cursada ainda.")
        return

    # Calcular média global e identificar reprovações
    soma_notas = 0.0
    reprovacoes = []
    aprovacoes_count = 0

    print("-" * 50)
    print(f"{'DISCIPLINA':<25} | {'NOTA':<5} | {'STATUS'}")
    print("-" * 50)

    for n in notas_do_aluno.values():
        soma_notas += n.nota
        
        status_materia = "Aprovado"
        if n.nota < 7.0:
            status_materia = "REPROVADO"
            reprovacoes.append(n)
        else:
            aprovacoes_count += 1
            
        print(f"{n.disciplina:<25} | {n.nota:.1f}  | {status_materia}")

    media_global = soma_notas / len(notas_do_aluno)
    print("-" * 50)
    print(f"MÉDIA GERAL DO CURSO (CR): {media_global:.1f}")

    # Lógica de Recuperação
    if reprovacoes:
        print("\n⚠️  ATENÇÃO: O aluno possui disciplinas abaixo da média.")
        resp = input("Deseja aplicar prova de recuperação/alterar nota? [S/N]: ").upper()
        
        if resp == 'S':
            alterar_nota_recuperacao(reprovacoes)
    else:
        print("\n Parabéns! Nenhuma pendência acadêmica.")

def alterar_nota_recuperacao(lista_reprovadas):
    print("\n--- APLICAR RECUPERAÇÃO ---")
    nome_disciplina = input("Digite o nome da disciplina para alterar a nota: ").strip().upper()
    
    nota_obj = None
    for n in lista_reprovadas:
        if n.disciplina == nome_disciplina:
            nota_obj = n
            break
    
    if nota_obj:
        nova_nota = float(input(f"Digite a nova nota final para {nome_disciplina}: "))
        nota_obj.nota = nova_nota 
        print(f"Sucesso! Nota de {nome_disciplina} atualizada para {nova_nota:.1f}.")
    else:
        print("Disciplina não encontrada na lista de reprovações.")