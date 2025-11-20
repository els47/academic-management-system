from dados import armazenamento
cursos = []

def cadastrar_cursos():
    while(True):

        # Recebendo valores do usuário
        codigo = int(input("Codigo: "))
        nome = str(input("Nome: ")).upper()

        cursos.append({"Codigo": codigo, "Nome": nome}) # Adicionando dicionário à lista

        print("Curso cadastrado!")

        # Confirmação de continuidade ou não
        r = ' '
        while r not in 'SN':
            r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if r == 'N':
            break
    # Iteração dos pares chave:valor e exibição para o usuário
    print('-'*50)
    print('               CURSOS CADASTRADOS               ')
    print('-'*50)
    for indice, curso in enumerate(cursos): # Percorrendo os dicionários na lista
        print(f"Codigo: {curso['Codigo']} | Nome: {curso['Nome']}") # Acessar os pares chave-valor dos dicionários
    print(''' ''')

cadastrar_cursos() 