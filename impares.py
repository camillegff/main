num = 1

max = int(input("Insira um número inteiro maior que 1: "))

print("números ímpares entre 1 e ", max , ":" )

while num <= max:
    if num %2==1: #usado para contagem de números ímpares
        print(num,   end=" ")
    num+=1
    