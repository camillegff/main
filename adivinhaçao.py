import random

num_sorteado = random.randint(1,10)
chute = None
tentativas = 0

while chute != num_sorteado:
    chute = int(input("Adivinhe o número entre 1 e 10: "))
    tentativas += 1

    if chute < num_sorteado:
        print("Tente um número maior na próxima! tentativas: ",tentativas)
    elif chute > num_sorteado:
        print("Tente um número menor na próxima! tentativas: ", tentativas)

print("Parabéns! voce adivinhou em: ", tentativas, "tentativas. o número sorteado foi: ",num_sorteado)
        

   
