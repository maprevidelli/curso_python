# Crie uma função que multiplica todo argumentos, não nomeados
# Retorne o total em uma variável e o mostre seu valor

def multiplic(*args):
    total = 1
    for item in args:
        total *= item
    return total    

numeros = 2, 5, 10, 3
resultado = multiplic(*numeros)
print(resultado)

print('==='* 30)
# Crie uma função que fale se o número é par ou ímpar, retorne se é par ou ímpar

def parimpar(x):
    if x % 2 == 0:
        return f'{x} é Par'
    return f' {x} é Ìmpar'

num = 3
resposta = parimpar(num)
print(resposta)