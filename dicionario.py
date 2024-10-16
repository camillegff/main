pessoa = {"nome": " pedro", "nome": "maria", " idade": 23, "cidade": "São Paulo"}

'''
pessoa["rua"] = "alguma rua 67" #método para adicionar um valor a lista.
pessoa.pop("rua") #método para remover um valor. 
'''

pessoa["idade"] = 90 #atualizar um valor já existente pela chave 
print(pessoa)
nome = pessoa.get("nome") #método get usado para coletar um valor do  dicionário com base na chave 
print(nome)



'''
print(pessoa.items())

print(pessoa["nome"])

for chave , valor in pessoa.items():
   print(chave + ":" +str(valor))

'''