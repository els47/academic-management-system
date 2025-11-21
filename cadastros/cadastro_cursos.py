
def cadastrar_cursos(cursos):
    while(True):

        # Recebendo valores do usuário
        # TODO: validar se código já existe
        codigo = int(input("Codigo: "))
        nome = str(input("Nome: ")).upper()

        existeCodigo = any(c["Codigo"] == codigo for c in cursos)
        existeNome = any(c["Nome"] == nome for c in cursos)

        

        if existeCodigo or existeNome:
            print("Curso já cadastrado. Tente novamente!")
        else:
            cursos.append({"Codigo": codigo, "Nome": nome}) # Adicionando dicionário à lista
            print("Curso cadastrado!")
            
        # Confirmação de continuidade ou não  
        if not deseja_continuar():
            break
        
    # Iteração dos pares chave:valor e exibição para o usuário
    print('-'*50)
    print('               CURSOS CADASTRADOS               ')
    print('-'*50)
    for indice, curso in enumerate(cursos): # Percorrendo os dicionários na lista
        print(f"Codigo: {curso['Codigo']} | Nome: {curso['Nome']}") # Acessar os pares chave-valor dos dicionários
    print(''' ''')

def deseja_continuar():
    while True:
        r = input("Deseja continuar? [S/N]: ").strip().upper()
        if r in ['S', 'N']:
            return r == 'S'   # True continua, False para



