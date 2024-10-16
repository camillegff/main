qnts_laranjas_pedro = 10 

print("Pedro tem 10 laranjas, retre quantas voce quiser. ")
qnts_laranjas_usuario = int(input("Quantas laranjas voce quer retirar? "))



qnts_laranjas_pedro = qnts_laranjas_pedro-qnts_laranjas_usuario


print("Sobraram: ",qnts_laranjas_pedro,"laranjas")
    
if qnts_laranjas_pedro >= 5:
    print("Pedro está feliz com a quantidade de laranjas! ")
elif qnts_laranjas_pedro < 5:
    print("Pedro está triste com poucas laranjas. ")
    
elif qnts_laranjas_pedro <= 0:
    print("Valor inválido! ")