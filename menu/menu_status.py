def exibir_status_geral(alunos, notas):
    while True:
        print("\n--- STATUS ACADÊMICO (MÉDIA GLOBAL & RECUPERAÇÃO) ---")
        
        # Buscar aluno
        matricula = input("Digite a Matrícula do aluno: ").strip()
        
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

            print(f"\n>> Aluno: {aluno_encontrado.nome} | Curso: {aluno_encontrado.curso}")

            # Filtrar notas aluno
            notas_do_aluno = {} 

            for n in notas:
                if n.aluno == aluno_encontrado.nome:
                    if n.disciplina not in notas_do_aluno or n.nota > notas_do_aluno[n.disciplina].nota:
                        notas_do_aluno[n.disciplina] = n

            if not notas_do_aluno:
                print("=== ERRO: Nenhuma disciplina cursada ainda.===")
                if deseja_sair(): 
                    break 
                else:
                    if not deseja_continuar(): 
                        break 
                    else:
                        continue
            else:
            
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
                if media_global >= 7.0:
                    print(f"MÉDIA GERAL DO CURSO (CR): {media_global:.1f} | STATUS: APROVADO NO CURSO")
                    print("\n O aluno não possui pendências")
                elif media_global < 7.0 and media_global >= 4.0:
                    print(f"MÉDIA GERAL DO CURSO (CR): {media_global:.1f} | STATUS: EM RECUPERAÇÃO")
                
                    # Lógica de Recuperação
                    if reprovacoes:
                        print("\n⚠️  ATENÇÃO: O aluno possui disciplinas abaixo da média.")
                        resp = input("Deseja aplicar prova de recuperação/alterar nota? [S/N]: ").upper()
                        
                        if resp == 'S':
                            alterar_nota_recuperacao(reprovacoes)
                        else:
                            print("\n Mantendo suas notas atuais. Aluno permanece em recuperação.")
                    else:
                        print("\n Aluno não atingiu a média, mas está com a pontuação mínima exigida.")
                else:
                    print(f"MÉDIA GERAL DO CURSO (CR): {media_global:.1f} | STATUS: REPROVADO NO CURSO")
                    print("\n Pontuação mínima exigida não atingida.")

                if not deseja_continuar():
                    break



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

                    
def deseja_continuar():
    while True:
        resp = input("\nDeseja verificar outro status? [S/N]: ").strip().upper() 
        if resp in ['S', 'N']: 
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")

def deseja_sair():
    while True:
        resp = input("\nDeseja retornar ao Menu Principal? [S/N]: ").strip().upper() # Retira os espaços e coloca todos em letra maiúscula
        if resp in ['S', 'N']: # Impede que o usuário digite outra letra além de S / N
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")