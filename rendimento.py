valor_depositado = float(input("Informe um valor para ser depositado: "))

def rendimento_mes(x):
    x *= 0.0070
    return x 

valr_rendindo = rendimento_mes(valor_depositado)
valor_total = valr_rendindo + valor_depositado

print("Após um mês seu valor", valor_depositado "rendeu:", valr_rendindo, ". Seu total sendo de: ", valor_total, "R$")

    