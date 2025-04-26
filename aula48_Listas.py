lista = [1978, True, 'Marco Antonio', 1.25, ['Racha-Cuca', 'Quase Nada']]
print('Lista simples: ', lista)
print(75*'=')
# mexer em algum lugar específico
lista[2] = 'Marco Antonio Previdelli'
del lista[3] # remove o item do índice
# adicionar no final
lista.append(50)
print('Lista alterada', lista)
lista.pop()
print(lista)
# inserir em um indice específico
lista.insert(1, 'Marlboro')
print(lista)
# somar ou unir listas
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
# uni-lás criando uma 3
lista_3 = lista_1 + lista_2 # chamado POLIMORFISMO quando algo se comporta diferente
# dependendo da situação, no caso o +
print(' = ' * 30)
print (lista_3)
# acresentar a uma das listas
lista_1.extend(lista_2)
print(lista_1)
"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)

