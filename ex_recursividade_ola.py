def repeticao(palavra:str, resultado:str):


    resultado += palavra + ", "
    print(resultado)

    entrada = input("Digite [s] - para continuar adicionando ou qualquer digíto para o programa parar. ")

    if entrada == "s":
        repeticao(palavra,resultado)

    else:
       print("Programa encerrado.")
       return resultado
    
codigo_inicial = ("Olá")      
codigo_final = repeticao(codigo_inicial, " ")
repeticao(codigo_final)