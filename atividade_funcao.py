'''
def numeros():
    for num in range(1,10+1):
        print(num)


numeros()
'''
'''
nome = "ana" #global

def nome_completo():
    sobrenome = "farias" #local
    print(nome)
    print(sobrenome)

print(nome) #a variavel global é possível printar tanto no começo, meio ou fim do programa, pois ela pertence a todos os blocos.
print(sobrenome) #é possível analisar que houve um erro, pois a variável local pertence ao bloco onde foi criada, ou seja, só acessamos ela de dentro.

'''

def a_mais_b(a,b):
    total = a+b

a_mais_b(5,6)


