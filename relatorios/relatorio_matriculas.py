# Pra emitir os relatório com todos os alunos matriculados em cada curso 
# e cada disciplina

def menu_relatorio_matriculas(alunos, cursos, disciplinas, notas):
    while True:
        print("\n--- RELATÓRIOS DE MATRÍCULAS ---")
        print("1 - Listar alunos por Curso")
        print("2 - Listar alunos por Disciplina")
        print("3 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            listar_alunos_por_curso(alunos, cursos)
        elif opcao == '2':
            listar_alunos_por_disciplina(alunos, disciplinas, notas)
        elif opcao == '3':
            break
        else:
            print("Opção inválida.")

def listar_alunos_por_curso(alunos, cursos):
    print("\n >> ALUNOS POR CURSO")
    for curso in cursos:
        print(f"\n CURSO: {curso.nome} (Cód: {curso.codigo})")
        qtd = 0
        for a in alunos:
            # vai verificar se o curso do aluno bate com o curso do loop
            # vai precisar mudar 'a.curso' se colocou com outro nome
            if str(a.curso) == curso.nome:
                print(f" - {a.nome} (Matrícula: {a.matricula})")
                qtd += 1

        if qtd == 0:
            print("(Nenhum aluno matriculado)")

def listar_alunos_por_disciplina(alunos, disciplinas, notas):
    print("\n >> ALUNOS POR DISCIPLINA")
    for disc in disciplinas:
        print(f"\n DISCIPLINA: {disc.nome}")
        encontrados = set()

        # irá procurar notas que tem a ver com essa disciplina
        for n in notas:
            nome_disc_nota = getattr(n.disciplina, 'nome', str(n.disciplina))

            if nome_disc_nota == disc.nome:
                encontrados.add(n.aluno)

        if encontrados:
            for nome_aluno in sorted(list(encontrados)):
                print(f" - {nome_aluno}")
        else:
            print("(Nenhum aluno com nota lançada.)")