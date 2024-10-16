lista = []
condicao = True

while condicao:
        
        opcao = int(input("1 - adicionar novo contato, 2 - exibir contatos,  3 - sair. "))

        if opcao == 1:
            print("Adicione um novo contato")
            nome = input("insira seu nome: ")
            telefone = (input("insira seu telefone: "))
            email = input("insira seu email: ")
            contato = (nome, telefone, email)
            lista.append(contato)
            print(lista)

        elif opcao == 2:
            print(lista)
    
        elif opcao == 3:
            print("Saindo...")
            break 

        else:
            print("Opção inválida!")