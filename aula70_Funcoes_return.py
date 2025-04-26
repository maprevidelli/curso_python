'''
Retorno de valores das funções (return)

'''
'''
def soma(x, y):
    print(x + y)
    
soma1 = soma(2, 2)# saída 4
soma2 = soma(3, 3)# saida 6
print(soma1 + soma2)# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# o print acima só funcionária se houvesse um return
'''
def soma(x, y):
    return(x + y)

soma1 = soma(2, 2)# sem saída
soma2 = soma(3, 3)# sem saída
print(soma1 + soma2)# saída: 10

print('===' * 15)
# as funções também aceitam condições aninhadas para return:

def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y


# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)# saída 4 - usa o ultimo return
print(soma2)# saída 6  - //
print(soma(11, 55))# saída [10, 20]