livros = [
    {"Título": "O Pequeno Príncipe", "Autor": "Antoine de Saint-Exupéry", "Ano de Lançamento": 1943, "Favorito": 0},
    {"Título": "Mr. Mercedes", "Autor": "Stephen King", "Ano de Lançamento": 2014, "Favorito": 0},
    {"Título": "Jogos Vorazes", "Autor": "Suzanne Collins", "Ano de Lançamento": 2008, "Favorito": 0},
    {"Título": "O Senhor das Moscas", "Autor": "William Golding", "Ano de Lançamento": 1997, "Favorito": 0},
    {"Título": "O Labirinto do Fauno", "Autor": "Cornelia Funke, Guilherme del Toro", "Ano de Lançamento": 2019, "Favorito": 0}


]


for x in livros:
    if x["Título"] == "Jogos Vorazes":
        x['Favorito'] = 1
    print(x)

    