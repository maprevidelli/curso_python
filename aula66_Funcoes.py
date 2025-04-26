#
"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(y=1, x=2, z=3)# saída: x=2 y=1 z=3 | x + y + z =  6
soma(1, y=2, z=5)# saída: x=1 y=2 z=5 | x + y + z =  8
# Repare que a partir do momento que nomeia= tem que nomear as demais

print(1, 2, 3, sep='-')

# Quando falamos em argumentos, estamos falando sobre os valores passados para as
# funções no ato da sua execução. Existem argumentos nomeados e argumentos posicionais.

# Argumentos nomeados recebem o nome do parâmetro antes do valor,
# argumentos posicionais recebem apenas o valor para preencher o parâmetro na ordem.

