# Enumerate - enumera itráveis (índice)
lista = ['Cavalo', 'Jumento', 'Camelo']
lista_enumerada = enumerate(lista)
#print(lista_enumerada) # Saída: <enumerate object at 0x7f55e3b58810>
lista_enumerada = list(enumerate(lista))
#print('Convertida para lista: ', lista_enumerada) # saída: [(0, 'Cavalo'), (1, 'Jumento'), (2, 'Camelo')]

# para acessar diretamente da lista use:
#for indice, nome in enumerate(lista):
#    print(indice, nome) # Saída: 0 Cavalo 1 Jumento 2 Camelo


for item in enumerate(lista):
     indice, nome = item
     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')