#Dicionário de informações sobre carros 

carros =[ 
    {"marca": "Toyota", "modelo": "Corolla", "ano": 2022, "cor": "prata", "preço": 25000},
    {"marca": "Honda", "modelo": "Civic", "ano": 2021, "cor": "preto", "preço": 28000},
    {"marca": "Ford", "modelo": "Mustang", "ano": 2020, "cor": "vermelho", "preço": 45000},
    {"marca": "Chevrolet", "modelo": "Camaro", "ano": 2021, "cor": "azul", "preço":50000},
    {"marca": "Tesla", "modelo": "Model S", "ano": 2023, "cor": "branco", "preço": 60000}
     
     
 ]

#Imprime informações sobre os carros

for carro in carros:
    print(f"Marca: {carro['marca']}, Modelo {carro['modelo']}, Ano: {carro['ano']}, Cor: {carro['cor']}, Preço: {carro['preço']}" )