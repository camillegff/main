print('1. idoso')
print('2. gestante')
print('3. cadeirante')
print('4. nenhum destes')
resposta = int(input('voce é: '))

if (resposta==1) or (resposta==2) or (resposta==3):
    print('voce tem direito a fila prioritária.')
else:
    print('voce nao tem direito a fila prioritária.')

