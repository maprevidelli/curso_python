# Listas


# Mexendo com sub-listas [[]]
print('='* 100, 'SUB-LISTAS')
# Como transferir um carro que está em uma sub-lista motos em veiculos:
veiculos = ['Sandero', 'Monza Hatch', 'Fiat Tipo', 'Kadet', ['Honda CBR 750',
'Yamaha 160', 'Mustang Shelby 500']]
print()
# copia o carro para fora da sub-lista (motos) para a Veiculos:
veiculos.insert(5, veiculos[4][2])
print(veiculos)
# deleta um item de uma sub-lista:
del veiculos[4][2]
print(veiculos)
