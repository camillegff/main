def lista_zerada():
    
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def lista_modificada(lista):
        print(lista)
        
        if len(lista) > 0:
            lista.pop()
            lista_modificada(lista)

        else:
            print("a lista está vazia.")
            return
    
    
    lista_modificada(lista)
    
lista_zerada()
