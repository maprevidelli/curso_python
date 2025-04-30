# Criar dicionário com quadrados dos números
quadrados = {x: x**2 for x in range(1, 6)}
print(quadrados)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filtrar itens
pessoa = {"nome": "Ana", "idade": 25, "cidade": "Rio"}
adulto = {chave: valor for chave, valor in pessoa.items() if chave != "cidade"}
print(adulto)  # {'nome': 'Ana', 'idade': 25}