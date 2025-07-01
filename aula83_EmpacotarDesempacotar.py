# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b) #Saída: 2 1

pessoa = {
    'nome': 'Maria',
    'sobrenome': 'Souza',
}

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2) # Saída: nome Maria
print(b1, b2) # Saída: sobrenome Souza



for chave, valor in pessoa.items():
    print(chave, valor) # nome Maria
                        # sobrenome Souza

print('=== separador 1 ===')                        

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
print(pessoas_completa) # {'nome': 'Maria', 'sobrenome': 'Souza', 'idade': 16, 'altura': 1.6}


# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)
print('=== separador 2 ===') 

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


mostro_argumentos_nomeados(nome='Joana', qualquer=123)
'''
NÃO NOMEADOS: ()
nome Joana
qualquer 123
'''
print('=== separador 3 ===') 

mostro_argumentos_nomeados(**pessoas_completa)

'''
NÃO NOMEADOS: ()
nome Maria
sobrenome Souza
idade 16
altura 1.6

'''

print('=== separador 4 ===') 


configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)
