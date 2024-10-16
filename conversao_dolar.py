dolar = int(input("Informe quantos doláres você quer trocar: "))

def conversao(dolar):
    real = dolar * 5
    return real

real = conversao(dolar)
print(f"Valor convertido! Você tem: {real} R$")