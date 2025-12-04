#esse é pra evitar de ficar cadastrando toda hora, é um saco

from modelos.curso import Curso
from modelos.disciplina import Disciplina
from modelos.professor import Professor
from modelos.aluno import Aluno
from modelos.nota import Nota

def popular_dados_teste(dados_sistema):
    print("\n Importando os dados do sistema...")
    
    # criando cursos
    c1 = Curso("101", "SISTEMAS PARA INTERNET")
    c2 = Curso("102", "CIÊNCIAS DA COMPUTAÇÃO")
    dados_sistema['cursos'].extend([c1, c2])
    
    # criando materias
    d1 = Disciplina("01", "TECNOLOGIA PARA FRONT-END")
    d2 = Disciplina("02", "TÓPICOS ESSENCIAIS PARA PROGRAMAÇÃO")
    d3 = Disciplina("03", "LÓGICA MATEMÁTICA")
    d4 = Disciplina("04", "INTERAÇÃO HUMANO-COMPUTADOR")
    d5 = Disciplina("05", "INTRODUÇÃO A PROGRAMAÇÃO")
    d6 = Disciplina("06", "REDES DE COMPUTADORES")
    d7 = Disciplina("07", "ARQUITETURA DE COMPUTADORES")
    d8 = Disciplina("08", "BANCO DE DADOS")
    d9 = Disciplina("09", "ESTRUTURA DE DADOS")
    d10 = Disciplina("10", "CYBERSEGURANÇA")
    dados_sistema['disciplinas'].extend([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10])
    
    # criando profs
    p1 = Professor("PROF01", "LEANDRO", d1, c1)
    p2 = Professor("PROF02", "NISSTON", d2, c1)
    p3 = Professor("PROF03", "JUAN", d3, c1)
    p4 = Professor("PROF04", "JUAN", d4, c1)
    p5 = Professor("PROF05", "DEMETRIUS", d5, c1)
    p6 = Professor("PROF06", "PRISCILLA", d6, c1)
    p7 = Professor("PROF07", "PRISCILLA", d7, c1)
    p8 = Professor("PROF08", "JOÃO ALBERTO", d8, c1)
    p9 = Professor("PROF09", "CAUE MOURA", d9, c1)
    p10 = Professor("PROF10", "FELIPE NETO", d10, c1)
    dados_sistema['professores'].extend([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
    
    # criando alunos pra testar em coisas dif
    # aluno aprovado (com notas altas)
    a1 = Aluno("1", "EDUARDA APROVADA", "SISTEMAS PARA INTERNET")
    # aluno em recuperação (notas médias)
    a2 = Aluno("2", "LISSA EM RECUPERAÇÃO", "SISTEMAS PARA INTERNET")
    # aluno reprovado (notas baixas)
    a3 = Aluno("3", "JOSÉ REPROVADO", "CIÊNCIAS DA COMPUTAÇÃO")
    # aluno concluinte (só pra testar o certificado)
    a4 = Aluno("4", "MARIA ANINHA", "SISTEMAS PARA INTERNET")
    
    dados_sistema['alunos'].extend([a1, a2, a3, a4])
    
    # lançamento de notas automático
    
    dados_sistema['notas'].append(Nota("EDUARDA APROVADA", d1, 10.0))
    dados_sistema['notas'].append(Nota("EDUARDA APROVADA", d2, 7.5))
    
    dados_sistema['notas'].append(Nota("LISSA EM RECUPERAÇÃO", d1, 4.9))
    dados_sistema['notas'].append(Nota("LISSA EM RECUPERAÇÃO", d2, 6.4))
    
    dados_sistema['notas'].append(Nota("JOSÉ REPROVADO", d1, 3.2))
    dados_sistema['notas'].append(Nota("JOSÉ REPROVADO", d2, 1.7))
    
    # as notas de Maria Aninha vou deixar faltando 1 pro certificado
    lista_discs_maria = [d1, d2, d3, d4, d5, d6, d7, d8, d9]

    for disc in lista_discs_maria:
        dados_sistema['notas'].append(Nota("MARIA ANINHA", disc, 9.8))

    print("✅ Dados importados com sucesso! (4 alunos, 2 cursos, 10 disciplinas)")
    print("Aluna 'MARIA ANINHA' Matrícula '4' possui 9 aprovações.")