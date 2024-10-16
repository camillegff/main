nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2)/2

def notas(valor):

    match valor:
        case x if x >= 0 and x <= 4:
            print("Reprovado.")
        case x if x >= 4.1 and x <= 7:
            print("Em exame.")
        case x if x >= 7.1 and x <= 10:
            print("Aprovado.")
        case _:
            print("Você não inseriu um número valído!")

notas(media)

            