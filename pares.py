numero = 1 
max = int(input('digite um inteiro maior que 1: '))

print("numeros pares entre 1 e ", max , ":")

while numero <= max:
    if numero%2==0: #usado na contagem de números pares
        print(numero,   end=" ")
    numero+=1
    