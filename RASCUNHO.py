livro = {
    'Nome' : 'The Last Aprentice',
    'Autor' : 'Joseph Delaney',
    'Editora' : 'Greenwillow Books',
     2006 : 'Ano',
    'Edição' : 3,
    'Capitulos' : 23,
    'Páginas' : 489,
    'Idioma' : 'Inglês',
}

'''

for chave in livro:
    print(f'{chave} = {livro[chave]}')
print('==' * 36)    
print(livro[chave])# saída: Inglês (último valor)


for chave in livro.items():# items = o par / values = somente os valores
    print(chave)
'''

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
     18 : 'idade',
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}

pessoa['peso'] = 90
print(pessoa['peso'])

pessoa['idade'] = 19
print(pessoa['idade'])





