vendedor = input("informe o nome do vendedor: ")
salario_fixo = int(input("informe o salário fixo do vendedor: "))
total_vendas =int(input("qual o total de vendas efetuadas do  mês: "))
COMISSAO = 15
salario_final = 0

def calculo_salario(vendas,salario,comissao):
    salario_total = salario + ((vendas*comissao)/100)
    return salario_total

salario_final = calculo_salario(total_vendas,salario_fixo,COMISSAO)

print(f"O vendedor {vendedor} tem um salário fixo de: {salario_fixo} R$")
print(f"No mês, ele vendeu {total_vendas} e com 15% d e comissão seu salário final é de {salario_final} R$ ")
