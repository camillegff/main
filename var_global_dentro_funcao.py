valor_total = 0

def minha_funcao(v):
    global valor_total
    valor_total += v

minha_funcao(5)
minha_funcao(5)
print(valor_total)