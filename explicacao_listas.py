a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]

'''
a.append(b) #ao utilizar o append, ele apenas adiciona toda a lista b dentro da lista a dentro do index 3.

print(a)  

'''
for item in b: #o for verifica os valores e faz a varredura do item no b. Depois adiciona um item da lista b por vez e separadamente dentro da lista a 
    a.append(item)  


print(a) 