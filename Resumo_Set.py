# Usando chaves // não é dicionário pq nao tem chave:valor
frutas = {"maçã", "banana", "laranja", "maçã"}
print(frutas)
# Usando a função set()
numeros = {1, 2, 3}
numeros.add(4) # {1, 2, 3, 4}
numeros.clear() # limpa o conjunto
print(numeros)

'''
numeros.remove(2) # {1, 3, 4}
numeros.remove(16) # KeyError: 16
numeros.discard(16) # não gera o erro
numeros.pop() # remove e retorna um aleatorio - se vaziu gera erro
'''


# Set vazio (precisa usar set(), não {} que cria dict)
vazio = set()

# Exemplo prático

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)           # União: {1, 2, 3, 4, 5}
print(A & B)           # Interseção: {3}
print(A - B)           # Diferença: {1, 2}
print(A ^ B)           # Diferença simétrica: {1, 2, 4, 5}

A.update({4, 5})       # A → {1, 2, 3, 4, 5}
print(A.isdisjoint({6, 7}))  # True (não há elementos em comum)