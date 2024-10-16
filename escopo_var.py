'''
x = 10

def minha_funcao():
    y = 20
    print(y) #y está em escopo local (de dentro da função)
    print(x) #x está em escopo global (de fora da função)

minha_funcao()

print(y) #código quebra por y não ser localizado de fora do bloco 'minha_funcao()'

'''

x = 300


def minha_funcao():
    #global x 
    x = 200
    print(x)
minha_funcao()

print(x)