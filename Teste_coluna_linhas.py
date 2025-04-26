linhas = 2
colunas = 2
 
linha = 1
while linha <= linhas:
    coluna = 1
    while coluna <= colunas:
        print(linha, coluna)
        coluna += 1
    linha += 1
# Veja que um looping por fora comana a linha (por ser definida como inicial), uma gira
# dentro da outra pra ir completando o limite de linha e coluna definidas    