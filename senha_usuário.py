condicao = True
senha = "09876"
count = 0

while condicao:
    entrada = input("Digite a senha: ")
    if entrada == senha:
        print('Senha correta!')
        condicao = False
    else:
        print("senha inválida, voce ainda tem: ",3-count," tentativas.")
        count += 1

    if count == 4:
        print('ACESSO BLOQUEADO.')

    

    




      

    