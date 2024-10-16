produto = int(input("digite um codigo dentre 100[cachorro quente] 101[bauru simples] 102[bauru com ovo] 103[hamburguer] 104[cheeseburguer] 105[refrigerante]: "))
quantidade = int(input("informe a quantidade desejada do produto: "))

def cardapio(item):

    match item:
        case 100:
            cachorro_quente = 1.70
            return cachorro_quente
        case 101:
            bauru_simples = 2.30
            return bauru_simples
        case 102:
            bauru_com_ovo = 2.60
            return bauru_com_ovo
        case 103:
            hamburguer = 2.40
            return hamburguer
        case 104:
            cheeseburguer = 2.50
            return cheeseburguer
        case 105:
            refrigerante = 1.00
            return refrigerante
            
v_total = cardapio(produto)*quantidade

print(f"total deu {v_total}")