valor = int(input("Digite um valor: "))

def produtos(codigo):
    
    match codigo:
        case x if x == 1:
            print("Alimento não-perecível.")
        case x if x == 2 or x == 3 or x == 4: 
            print("Alimento perecível.")
        case x if x == 5 or x == 6:
            print("Vestuário")
        case x if x == 7:
            print("Higiene Pessoal.") 
        case x if x >= 8 and x <= 15:
            print("Limpeza e Utensílios Domésticos.")
        case _:
            print("Código Inválido.")

produtos(valor)
          