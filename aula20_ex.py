primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')
if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior que {segundo_valor=}')
elif segundo_valor > primeiro_valor:
    print(f'{segundo_valor=} é maior que {primeiro_valor=}')
elif segundo_valor == primeiro_valor:
    print(f'{primeiro_valor=} é igual a {segundo_valor=}')
else:
    print('Tudo cagado ai')
print('\033[4;34;41m Fim do Programa \033[m')    
        