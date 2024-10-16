import time

minutos = 5
segundos = 0

print(f"{minutos}:{segundos}")
for i in range((minutos*60)+segundos):
    time.sleep(0.1)  
   
    if minutos >0:
        if segundos >0:
            segundos = segundos-1
        else:
            segundos = 59
            minutos = minutos-1
    elif minutos ==0 and segundos>0:
         segundos = segundos-1
    else:
        print("erro inesperado")

    print(f"{minutos}:{segundos}")
    if minutos == 0 and segundos == 0:
            print("acabou")
