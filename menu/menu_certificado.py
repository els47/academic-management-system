def gerar_certificado(alunos, notas):
    print("\n--- EMISSÃO DE CERTIFICADO ---")
    matricula = input("Digite a Matrícula do aluno: ").strip()

    # Busca aluno
    aluno_encontrado = None
    for a in alunos:
        if str(a.matricula) == matricula:
            aluno_encontrado = a
            break
    
    if not aluno_encontrado:
        print("Aluno não encontrado.")
        return

    # Contar aprovações (Usa um set pra não repetir matéria)
    disciplinas_aprovadas = set()
    
    for n in notas:
        if n.aluno == aluno_encontrado.nome and n.nota >= 7.0:
            disciplinas_aprovadas.add(n.disciplina) 

    # Contar quantos itens tem no set
    qtd_aprovadas = len(disciplinas_aprovadas)

    print(f"\nAnalisando histórico de: {aluno_encontrado.nome}")
    print(f"Quantidade de Aprovações: {qtd_aprovadas}")
    
    # Pra ver os nomes, transforme o set em string
    if qtd_aprovadas > 0:
        print(f"Matérias: {', '.join(disciplinas_aprovadas)}")

    # Mínimo 10 matérias
    MINIMO_PARA_FORMATURA = 10

    if qtd_aprovadas >= MINIMO_PARA_FORMATURA:
        print("\n" + "="*40)
        print("🎓  CERTIFICADO DE CONCLUSÃO  🎓")
        print("="*40)
        print(f"Certificamos que {aluno_encontrado.nome}")
        print(f"Concluiu o curso de {aluno_encontrado.curso}")
        print("Estando apto(a) a exercer a profissão.")
        print("="*40)
    else:
        falta = MINIMO_PARA_FORMATURA - qtd_aprovadas
        print(f"\n❌ Certificado Bloqueado.")
        print(f"O aluno precisa concluir mais {falta} disciplinas com nota >= 7.0.")