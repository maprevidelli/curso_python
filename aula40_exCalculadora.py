"""
Calculadora com While
"""
# Veja que com o Try vc mata ter que analisar os erros caso for digitado algo indevido
while True:
    try:
        num1 = float(input('Entre com o primeiro número: '))
        oper = input('Entre com a operação [+], [-], [*], [/]: ')
        num2 = float(input('Entre com o segundo número: '))
    except:
        print('Você não digitou o que foi pedido!')
        continue
    if oper == '+':
        print(f'A soma entre {num1} + {num2} é = {num1 + num2}')
    elif oper == '-':
        print(f'A subtração entre {num1} - {num2} é = {num1 - num2}')
    elif oper == '*':
        print(f'A multiplicação entre {num1} * {num2} é = {num1 * num2}')
    elif oper == '/':
        print(f'A divisão entre {num1} / {num2} é = {num1 / num2}')
    else:
        print('Operação errada!')
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        print('Calculadora encerrada, obrigado!')
        break

    
'''
versão do Professor, veja como usa o True para validação:

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ###

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
'''