lista_frase = []

def nova_frase(s):
   
    lista_frase.append(s)
    print("deseja continuar adicionando [s] ou [n]")
    op = input(" ")
    if(op) == "s":
        entrada = input("digite uma frase: ")
        nova_frase(entrada) #recursão é quando uma função chama ela mesma.
    else:
        print("fim..")
        return


entrada = input("digite uma frase: ")

nova_frase(entrada) 
