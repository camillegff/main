sexo = str(input("digite M para masculino ou F para feminino "))
idade_contri_inicial = int(input("com qual idade você começou a contribuir? "))
TEMPO_NECESSARIO_MIN = 25
TEMPO_NECESSARIO_MAX = 40
idade_mulher_min_aposentar = 0
idade_mulher_aposentar_max_beneficio = 0
def calc_contri_mulher():
    global TEMPO_NECESSARIO , idade_mulher_min_aposentar , idade_mulher_aposentar_max_beneficio
    
    idade_mulher_min_aposentar = idade_contri_inicial + TEMPO_NECESSARIO_MIN
    idade_mulher_aposentar_max_beneficio = idade_contri_inicial + TEMPO_NECESSARIO_MAX

    if idade_mulher_min_aposentar <62:
        while idade_mulher_min_aposentar < 62:
             idade_mulher_min_aposentar += 1

    print(f"levando em conta sua contribuição inicial aos {idade_contri_inicial}, sua idade mínima para se aposentar é aos {idade_mulher_min_aposentar}.")

    contribuicao_minima_desenvovida = idade_mulher_min_aposentar - idade_contri_inicial

    if contribuicao_minima_desenvovida >= 25 and contribuicao_minima_desenvovida <= 29:
        print(f"com está idade você terá direito a 70% do beneficio")
    elif contribuicao_minima_desenvovida >= 30 and contribuicao_minima_desenvovida <= 34:
        print(f"com está idade você terá direito a 77,5% do beneficio")
    elif contribuicao_minima_desenvovida >= 35 and contribuicao_minima_desenvovida <= 39:
        print(f"com está idade você terá direito a 87,5% do beneficio")
    elif contribuicao_minima_desenvovida >= 40:
        print(f"com está idade você terá direito a 100% do beneficio")

    print(f"levando em conta sua contribuição inicial aos {idade_contri_inicial}, sua idade para receber o beneficio máximo 100% da aposentadoria é aos {idade_mulher_aposentar_max_beneficio} anos.")        
if sexo == "f" or sexo == "F":
    calc_contri_mulher()
else:
    print("você digiotu errado as opções")