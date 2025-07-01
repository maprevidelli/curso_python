# Listas
# Mexendo com sub-listas [[]]

# transferir um carro que está em uma sub-lista motos para a veiculos:
veiculos = ['Sandero', 'Monza Hatch', 'Fiat Tipo', 'Kadet', ['Honda CBR 750',
'Yamaha 160', 'Mustang Shelby 500']]
print('Lista Original: ', veiculos)
print()
# copia o carro para fora da sub-lista (motos) para a Veiculos:
veiculos.insert(5, veiculos[4][2])
print('Veiculos: ',veiculos)
# depois deleta um item de uma sub-lista:
del veiculos[4][2]
# Arruma para as motos ficarem no final:
veiculos.insert(5, 4)
print('Veiculos e [motos]: ',veiculos)


# Separar as Listas
print('=' * 40)

# para funcionar cole a original aqui:
veiculos = ['Sandero', 'Monza Hatch', 'Fiat Tipo', 'Kadet', ['Honda CBR 750',
'Yamaha 160', 'Mustang Shelby 500']]

carros = veiculos[0:4]
motos = veiculos[4]
carro = motos.pop(2)
carros.append(carro)
print('Veiculos: ', carros)
print('Motos', motos)