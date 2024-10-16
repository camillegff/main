#adicionar informação em uma lista 

#lista.append()

#continuar condição 
#while 

#exibir opções para o usuário
#print()


lista = []
condicao = True



while condicao:
    opcao = input("1 - para exibir a lista, 2 - sair e 3 - continuar adicionando. ")

    if opcao == "1":
        print(lista)

    elif opcao == "2":
        print("saindo...")
        break
        condicao = False #atribuição a partir da segunda vez = reatribuição 

    elif opcao == "3":
        print("continuar adicionando...")
        valor = input("digite um valor para adicionar: ")
        lista.append(valor)

    else:
        print("Número inválido!")
    