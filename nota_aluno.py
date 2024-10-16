nota = float(input('Digite uma nota: '))

if nota >= 0.0 and nota <= 10.0:
    if nota<6.0 and nota>=0:
        print('nota F.')
    elif nota>=6.0 and nota<=7.0:
        print('nota D.')
    elif nota>=7.0 and nota<=8.0:
        print('nota C')
    elif nota>=8.0 and nota<=9.0:
        print('nota B.')
    elif nota>=9.0 and nota<=10.0:
        print('nota A.') 
else:
    print('Nenhuma nota inserida entre o valor estipulado (0 até 10) !')