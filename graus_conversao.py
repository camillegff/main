graus = int(input("informe quantos graus está fazendo hoje: "))

def conversao(graus):
    fahrenheit = (9*graus+160)/5
    return fahrenheit

fahrenheit = conversao(graus)
print(f"A temperatura está de {fahrenheit}F")
