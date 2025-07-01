# usar uma Lista como chaves e depois pedir os valores em um dicionario
lista = ['Nome', 'Sobrenome', 'Data Nascimento', 'Cidade', 'Escolaridade',
'Estado Civil', 'Filhos','Profissão']
print()
dicionario = {}
for chave in lista:
    valor = input(f'Entre com a informação ({chave}): ')
    dicionario[chave] = valor
print('='*10)    
print('Cadastro efetuado!')
print('='*10)
print('Confira as informações digitadas')
print()

for chave in dicionario:
    print(f'{chave}: {dicionario[chave]}')

from datetime import datetime

data_atual = datetime.now()
print("Data e hora atuais:", data_atual)
