"""
for in com listas
"""
'''
lista = ['Maria', 'Helena', 'Luiz']

for nome in lista:
    print(nome, type(nome))
# Mostou que a lista é um iterável

# Exercicio mostrar o indice
contador = 2
while contador >= 0:
    palavra = lista.pop()
    print(contador, palavra)
    contador -= 1'
'''

"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = (len(lista))
print(f'='* 10)
print(indices)
'''
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
'''
###

for indice in enumerate(lista):
    print(indice, lista)
