# isinstace - para saber se objeto é de determinado tipo
#  - Sintaxe - 
# isinstance(objeto, classe)
# False ou True


lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
    else:
        print('OUTRO')
        print(item)

'''
Quando usar
Use isinstance() quando:

> Você precisa verificar tipos de forma flexível (considerando herança)

> Quer verificar contra múltiplos tipos possíveis

> Está trabalhando com hierarquias de classes complexas

Evite usar quando:

> Você precisa de uma verificação exata de tipo (nesse caso, use type(obj) is Classe)

> Está verificando tipos primitivos muito simples (nesse caso, type() pode ser suficiente)

'''        