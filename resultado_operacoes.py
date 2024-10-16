def calculos(x,y):
    soma = x + y
    subtracao = x - y
    multiplicacao = x * y 
    divisao = x / y
    total = soma, subtracao, multiplicacao, divisao
    return total 

total = calculos(8,3)
print(total)