def exibir_relatorio_geral(alunos, cursos, disciplinas, professores):
    print(f"\n--- RELATÓRIO GERAL ---")
    print("-" * 100)
    print(f"{'ALUNOS':<20} | {'PROFESSORES':<20} | {'CURSOS':<20} | {'DISCIPLINAS':<20}")
    print("-" * 100)

    print(f"{len(alunos):<20} | {len(professores):<20} | {len(cursos):<20} | {len(disciplinas):<20}")

    if deseja_sair():
        return
    else:
        exibir_relatorio_geral

def deseja_sair():
    while True:
        resp = input("\nDigite 'SAIR' para retornar ao Menu: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['SAIR']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'SAIR'
        print("Opção inválida. Digite 'SAIR'")