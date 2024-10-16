valor_depositado = 0 

valor_depositado += float(input(f"insira um valor para ser depositado: "))

def rendimento_mes(x):
    x *= 0.0070 
    return x 

valor_rendido = rendimento_mes(valor_depositado)
total = valor_depositado + valor_rendido
print(f"Com um mês de rendimento, seu valor rendido mais o que já foi depositado é de: {total} R$")