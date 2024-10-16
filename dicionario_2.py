'''
pessoa = {"nome": "ana", "idade": 30, "cidade": "sao paulo"}
bixos_da_ana = {"cachorro": "freud", "gato": "lucas"}

pessoa.update(bixos_da_ana) #joga os itens de um dicionário para dentro do outro
print(pessoa)
'''

#copiar dicionário

import copy 

login = {'joao'  : 'senha',
         'maria' : '123456',
        'zezinho'  : 'restart',
       }

backup = copy.deepcopy(login)
print(backup)

login['zezinho'] = 'ironmaiden'

print(login)
print(backup)


capitais = {
        ('Brasil','Rio de Janeiro'): 'Rio de Janeiro'
}

print(capitais)
print(capitais['Brasil', 'Rio de Janeiro'])
print(capitais.get('Brasil', 'Rio de Janeiro'))
print(capitais.keys ())

