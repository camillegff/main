total = float(input('Premio total da Mega: '))
num = int(input('Número de gaanhadores: '))

#print('Cada um  vai ficar com R$ %.2f' % (total/num))

print(f'O premio total foi R${total:.2f} para {num} ganhadores, onde cada um ficou com R${total/num:.2f}')
