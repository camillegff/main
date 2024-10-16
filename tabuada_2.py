count = 0 
condicao = True


while condicao:
    count = 0
    entrada = int(input('informe um número: '))

    while count <= 10:
        print(entrada, " x ", )

    
        
    opcao = input('\n 1 - para informar o novo número e digite 2 - para sair. ')

    if opcao == "1":
        print('continuando...')
    elif opcao == "2":
        condicao = False
    else:
        print("número inválido.")
