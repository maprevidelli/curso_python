# Lista de compras simples
lista = []
def cabecalho():
	print('\n--------  Bem vindo ao Lista de compras simples! ------ ')
	print('\nA. Adicionar produto')
	print('B. Remover produto')
	print('C. Pesquiar produto')
	print('D. Sair do programa')
	
def unidade():
	print('A. Quilograma')
	print('B. Grama')
	print('C. Litro')
	print('D. Mililitro')
	print('E. Unidade')
	print('F. Metro')
	print('G. Centímetro')
	opcao_medida = input('\nSelecione a unidade de medida: ')
	opcao_medida = opcao_medida.lower()
	if opcao_medida == 'a':
		tipo = 'Quilos'
	if opcao_medida == 'b':
		tipo = 'Grama'
	if opcao_medida == 'c':
		tipo = 'Litro'
	if opcao_medida == 'd':
		tipo = 'Mililitro'
	if opcao_medida == 'e':
		tipo = 'Unidade'
	if opcao_medida == 'f':
		tipo = 'Metro'
	if opcao_medida == 'g':
		tipo = 'Centímetros'
	if opcao_medida not in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
		print('Opção inválida')
	return(tipo)
	
while True:
	cabecalho()
	opcao = input('\nDigite a opção desejada: ')
	opcao = opcao.lower()
	if opcao not in ['a', 'b', 'c', 'd']:
		print('\n>>>>>>>> Opção Inválida!')
		continue
		
	if opcao == 'd':
		print('\n ==== Grato por usar a Lista de compras simples ====')
		break
	elif opcao == 'a':
		print('\n==== Adicionar produto ====')
		nome = input('Nome do produto: ')
		lista.append(nome)
	try:
		unidade()
	except:
		continue
		lista.append(unidade())
		quantia = float(input('Digite a quantidade: '))
		lista.append(quantia)
		descri = input('Digite a descrição (até 10 caracteres) do produto: ')[:10]
		lista.append(descri)
		print(lista)
	if opcao == 'b':
		# Remover produto
		print('opção B computada')
	elif opcao == 'c':
		# Pesquisar o produto
		print('opção C computada')
	else:
		print('================ Opção inválida! =================')
		continue
		
