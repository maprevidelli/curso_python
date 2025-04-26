'''
args - são os argumentos não nomeados
* - *args (empacotamento  desempacotamento)

'''

# Lembre de desempacotamento
x, y, *resto = 1, 2, 3, 4, 5 #isso é uma Tupla
print(x, y, resto)#saída: 1 2 [3, 4, 5] -> criou uma Lista chamada "Resto" pra separar/ empacotou-a
print('Não quero', resto)

def soma(*args):
    print(args)

soma(1, 2, 3, 4, 5, 6, 7, 8)# especifiquei argumentos para o parâmetro *args criar a Tupla
# se precisa-se de uma lista, é só converter: args = list(args)

##### REVER:
print('===' * 30)
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

numeros = 550, 1550, 2550
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))# aqui mostra que já tem uma função em python para isso, o SUM
# print(*numeros)