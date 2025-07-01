# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},
# ]
# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)

# Explicação do DeepSeek:

'''
Em Python, uma função lambda (ou função anônima) é uma função pequena e sem nome,
 definida usando a palavra-chave lambda. Ela é usada para criar funções simples e
   temporárias, geralmente para operações rápidas onde uma função completa seria
     desnecessária.

lambda argumentos: expressão

lambda: Palavra-chave que define a função anônima.
argumentos: Parâmetros da função (separados por vírgula se houver mais de um).
expressão: O que a função retorna (não usa return explicitamente).

Características:

Sem nome: Não é definida com def, mas pode ser atribuída a uma variável.
Uma única expressão: Só pode conter uma linha de código.
Útil para funções simples: Comumente usada com map(), filter(), sorted(), etc.

'''

# Exemplo:
dobro = lambda x: x * 2
print(dobro(5))  # Saída: 10

# Equivalente a:
def dobro(x):
    return x * 2

# Outro Exemplo:
tuplas = [(1, 'Z'), (3, 'A'), (2, 'B')]
ordenado = sorted(tuplas, key=lambda x: x[1])
print(ordenado)  # Saída: [(3, 'A'), (2, 'B'), (1, 'Z')]

# Outro Exemplo:
soma = lambda a, b: a + b
print(soma(3, 7))  # Saída: 10

# Minha criação:
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
# criou uma função (DEF) em uma variável em apenas 1 linha
desempacota = lambda lista, x: lista[x]
checados = set()
primeiro = -1
for numero in range(1, len(lista_de_listas_de_inteiros)):
    print()
    print(f'Esta é a sublista: {numero}= {desempacota(lista_de_listas_de_inteiros, numero)}')
    if numero in checados:
        primeiro = numero
        break
    checados.add(numero)

print(checados)