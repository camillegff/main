cadastro = []
count = 0

while len(cadastro) <= 3:
    entrada = (input("informe seu nome para o cadastro: "))
    cadastro.append(entrada)
    print("usuário adicionado!")
    count += 1


entrada = input("cadastre outro nome: ")

if entrada in cadastro:
    print(f"{entrada} já está na lista de cadastrados.")
    
if entrada not in cadastro:
    print(f"{entrada} não está na lista de cadastrados.")


