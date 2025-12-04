from datetime import date

def gerar_certificado(alunos, notas):
    while True:
        print("\n--- EMISSÃO DE CERTIFICADO ---")
        matricula = input("Digite a Matrícula do aluno: ").strip()

        # Busca aluno
        aluno_encontrado = None
        for a in alunos:
            if str(a.matricula) == matricula:
                aluno_encontrado = a
                break
        
        if not aluno_encontrado:
            print("=== ERRO: Aluno não encontrado. ===")
            if deseja_sair(): 
                break 
            else:
                if not deseja_continuar(): 
                    break 
                else:
                    continue
        else:

            # Contar aprovações (Usa um set pra não repetir matéria)
            disciplinas_aprovadas = set()
            
            for n in notas:
                if n.aluno == aluno_encontrado.nome and n.nota >= 7.0:
                    nome_disc = getattr(n.disciplina, 'nome', str(n.disciplina))
                    disciplinas_aprovadas.add(nome_disc)

            # Contar quantos itens tem no set
            qtd_aprovadas = len(disciplinas_aprovadas)

            print(f"\n Analisando histórico de: {aluno_encontrado.nome}")
            print(f"Quantidade de Aprovações: {qtd_aprovadas}")
            
            # Pra ver os nomes, transforme o set em string em ordem alfabética
            if qtd_aprovadas > 0:
                lista_nomes = sorted(list(disciplinas_aprovadas))
                print(f"Matérias Aprovadas: {', '.join(lista_nomes)}")

            # Mínimo 10 matérias
            MINIMO_PARA_FORMATURA = 10

            if qtd_aprovadas >= MINIMO_PARA_FORMATURA:
                # Aqui faz o formato de data DD/MM/AAAA ao invés de AAA/MM/DD
                data_hoje = date.today().strftime("%d/%m/%Y")

                print("\n" + "="*60)
                print("🎓  CERTIFICADO DE CONCLUSÃO  🎓".center(60))
                print("="*60)
                print("\n Certificamos que:")
                print(f"{aluno_encontrado.nome.upper()}".center(60))
                print("\n Concluiu o curso de:")
                print(f"{aluno_encontrado.curso}".center(60))
                print("\n Estando apto(a) a exercer a profissão.")
                print(f"\n Data de Emissão: {data_hoje}") # formato br
                print("\n\n Assinatura: ______________________________________.")
                print("            Diretor Acadêmico")
                print("="*60)

                # Adicionei opção de sair dps de gerar o certificado
                if not deseja_continuar():
                    break

            else:
                falta = MINIMO_PARA_FORMATURA - qtd_aprovadas
                print(f"\n❌ Certificado Bloqueado.")
                print(f"O aluno precisa concluir mais {falta} disciplinas com nota >= 7.0.")
                print("Critério mínimo: 10 disciplinas aprovadas.")

                if deseja_sair(): 
                    break 
                else:
                    if not deseja_continuar(): 
                        break 
                    else:
                        continue

def deseja_continuar():
    while True:
        resp = input("\nDeseja emitir outro certificado? [S/N]: ").strip().upper() 
        if resp in ['S', 'N']: 
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")

def deseja_sair():
    while True:
        resp = input("\nDeseja retornar ao Menu Principal? [S/N]: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['S', 'N']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")