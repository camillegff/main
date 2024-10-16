rodada = 0
lista_n = []

while len(lista_n) < (10):
    entrada = int(input(f"(rodada{rodada}) - insira um número: "))
    lista_n.append(entrada)
    rodada += 1

print(f"Ordem original: {lista_n}")

lista_n.reverse()

print(f"Ordem inversa: {lista_n}")

