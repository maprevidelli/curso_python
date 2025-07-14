
produtos = [
    {'nome': 'Notebook', 'preco': 3500.00, 'estoque': 5, 'categoria': 'eletrônicos'},
    {'nome': 'Camiseta', 'preco': 49.90, 'estoque': 0, 'categoria': 'vestuário'},
    {'nome': 'Smartphone', 'preco': 1999.99, 'estoque': 10, 'categoria': 'eletrônicos'},
    {'nome': 'Arroz', 'preco': 22.50, 'estoque': 100, 'categoria': 'alimentos'},
    {'nome': 'Fone de Ouvido', 'preco': 150.00, 'estoque': 3, 'categoria': 'eletrônicos'},
    {'nome': 'Calça Jeans', 'preco': 120.00, 'estoque': 0, 'categoria': 'vestuário'},
]

'''
Sua tarefa é:

1 - Filtrar produtos com estoque maior que 0 (apenas produtos disponíveis).

2 - Aplicar um desconto de 10% nos produtos da categoria "eletrônicos".

3 - Criar uma nova lista de dicionários contendo apenas 'nome', 'preco_final' 
    (com desconto, se aplicável) e 'categoria'.

'''
# Solução 1:
produtos_nao_zerdos = [produto for produto in produtos if produto['estoque'] > 0]

for iten in produtos_nao_zerdos:
    print(iten)


print()
# Solução 2:
eletronicos = [pr for pr in produtos if pr['categoria'] == 'eletrônicos']
for produto in eletronicos:
    produto['preco'] *= 0.90

for produto in eletronicos:
    print(f'{produto['nome']} : R${produto['preco']:.2f}')

print()
# Solução 3: (Nessa altura os eletronicos já estão com desconto)
for dicionario in produtos:
    if 'estoque' in dicionario:
        del dicionario['estoque']
        print(f'{dicionario['nome']} : R${dicionario['preco']:.2f} : {dicionario['categoria']}')
