from modelos.nota import Nota

def cadastrar_notas(notas, alunos, disciplinas):
    while True:
        print("\n--- CADASTRO DE NOTAS ---")

        # Aluno já cadastrado?
        print(">> Cadastro do Aluno")
        matricula_input = input("Matrícula: ").strip()
        nome_input = str(input("Nome Completo: ")).strip().upper()

        aluno_encontrado = None 

        for a in alunos:
            if (a.matricula) == matricula_input and a.nome == nome_input:
                aluno_encontrado = a
                break

        if not aluno_encontrado:
            print(f"Erro: Aluno não encontrado (Matrícula: {matricula_input} | Nome: {nome_input}).")
            print("Verifique se o aluno está cadastrado na disciplina/curso corretamente.")
            if deseja_sair(): 
                break 
            else:
                if not deseja_continuar(): 
                    break 
                else:
                    continue 
        else:
            print(f"Aluno verificado: {aluno_encontrado.nome} (Matrícula: {aluno_encontrado.matricula})")

            # Aluno já cadastrado, verificar se a disciplina já está cadastrada
            codigo_disciplina = str(input("Código da Disciplina: ")).strip().upper()

            disciplina_existe = False
            for d in disciplinas:
                if d.codigo == codigo_disciplina:
                    disciplina_existe = True
                    break
            
            if not disciplina_existe:
                print(f"ERRO: A disciplina '{codigo_disciplina}' não existe! Cadastre-a primeiro.")
                if deseja_sair(): 
                    break 
                else:
                    if not deseja_continuar(): 
                        break 
                    else:
                        continue 
            
    
            else:
                try:
                    # Pedir nota AV1 e AV2
                    av1 = float(input("Nota AV1: "))
                    av2 = float(input("Nota AV2: "))
                    
                    # Calcula média
                    media = (av1 + av2) / 2
                    status = "Reprovado" 
                    nota_final = 0.0

                    # Implementar verificação de Status
                    if media >= 7.0:
                        status = "Aprovado"
                    else:
                        # Se < 7.0, prova Final
                        print(f"Média ({media:.1f}) abaixo de 7.0. Necessário Prova Final.")
                        nota_final = float(input("Nota da Prova Final: "))

                        # Substituir a nota mais baixa pela nota final
                        if av1 < av2:
                            av1 = nota_final # Substitui AV1 se for a menor
                        else:
                            av2 = nota_final # Substitui AV2 se for a menor
                        
                        # Recalcula a média
                        media = (av1 + av2) / 2
                        
                        # Final
                        if media >= 5.0:
                            status = "Aprovado na Final"
                        else:
                            status = "Reprovado"

                    # Perguntar sobre Certificado (só se aprovado)
                    msg_certificado = "Não emitido"
                    if "Aprovado" in status:
                        print(f"Aluno {status}! Média Final: {media:.1f}")
                        if input("Deseja emitir certificado de conclusão? [S/N]: ").upper() == 'S':
                            msg_certificado = "Emitido"
                            print("Certificado gerado com sucesso!")
                    
                    # Perguntar sobre Boletim (sempre)
                    if input("Deseja emitir o boletim? [S/N]: ").upper() == 'S':
                        print("\n" + "="*30)
                        print("       BOLETIM ESCOLAR")
                        print("="*30)
                        print(f"Aluno: {aluno_encontrado.nome}")                       
                        print(f"Disciplina: {codigo_disciplina}")
                        print(f"Média Final: {media:.1f}")
                        print(f"Situação: {status}")
                        print("="*30)

                    # Salva a média final
                    nova_nota = Nota(aluno_encontrado.nome, codigo_disciplina, f"{media:.1f}")                                              
                    notas.append(nova_nota)
                    print(f"Média final '{media:.1f}' cadastrada com sucesso!")

                except ValueError:
                    print("Erro: Digite apenas números para as notas!")

            if not deseja_continuar(): 
                break

    # Lista das notas
    if notas:
        print('-'*50)
        print('NOTAS CADASTRADAS'.center(50))
        print('-'*50)
        for n in notas:
            print(f"Aluno: {n.aluno} | Disciplina:[{n.disciplina}] | Média: {n.nota}")
        print('-'*50)


def deseja_continuar():
    while True:
        resp = input("Deseja cadastrar outra nota? [S/N]: ").strip().upper() 
        if resp in ['S', 'N']: 
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")

def deseja_sair():
    while True:
        resp = input("Deseja retornar ao Menu de Cadastro? [S/N]: ").strip().upper() 
        if resp in ['S', 'N']: 
            return resp == 'S'
        print("Opção inválida. Digite S ou N.")