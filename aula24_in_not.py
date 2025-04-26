nome = input('Entre com uma palavra: ')
encontrar = input('O que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')    
    