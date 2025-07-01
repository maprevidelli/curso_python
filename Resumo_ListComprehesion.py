'''
List comprehension (compreensão de lista) é uma forma concisa e elegante de criar
 listas em Python. Ela permite que você crie uma nova lista aplicando uma expressão
   a cada item de um iterável (como lista, tupla, string, etc.) de forma mais compacta
     que um loop tradicional.

'''

# Sintaxe básica:
# nova_lista = [expressão for item in iterável]

# Exemplo:
# Quadrados dos números de 0 a 9
quadrados = [x**2 for x in range(10)]
print(quadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Com condição:
# nova_lista = [expressão for item in iterável if condição]

# Números pares de 0 a 9
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

# Aninhada:
# Produto cartesiano de duas listas
cores = ['vermelho', 'verde', 'azul']
tamanhos = ['P', 'M', 'G']
produtos = [(cor, tamanho) for cor in cores for tamanho in tamanhos]
print(produtos)

# Exemplo mais complexo:
# Matriz transposta
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposta = [[linha[i] for linha in matriz] for i in range(3)]
print(transposta)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

