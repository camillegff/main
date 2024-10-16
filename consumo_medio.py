distancia_total = float(input("Qual a distância total percorrida pelo autómovel: "))
combustivel_gasto = float(input("Informe o total de combustível gasto: "))


def consumo_medio(distancia_total,combustivel_gasto):
    total = distancia_total/combustivel_gasto
    return total

total = consumo_medio(distancia_total,combustivel_gasto)
print(f"O consumo total do seu automovél é de: {total:.2f}")
