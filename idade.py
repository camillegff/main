idade = int(input("digite sua idade: "))

if idade >= 18 and idade <= 65:
    print("voce é obrigado a votar, se nao paga multa. idade informada: ",idade)
else:
    print("voce nao é obrigado a votar. idade informada:",idade)