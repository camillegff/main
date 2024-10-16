valor = int(input("Digite um valor entre 1[media] 2[diferenca] 3[produto] 4[divisao]: "))
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

def lista_escolhas(escolha):
    
    match escolha:
        case 1:
            media = (num1+num2)/2
            print(media)
        case 2:
            diferenca = num1-num2
            print(diferenca)
        case 3:
            produto = num1*num2
            print(produto)
        case 4:
            divisao = num1/num2
            print(divisao)
        case _:
            print("Erro na execução do programa.")

lista_escolhas(valor)

