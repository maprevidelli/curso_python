# calculo de IMC
nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura (em metros)'))
peso = int(input('digite seu peso (em kg)'))
imc = float(peso / (altura * altura))
print('{} tem {} de altura e pesa {}'.format(nome, altura, peso))
print('Seu IMC é: {:.2f}'.format(imc))
# f-string é um outro modo
resposta_2 = f'Olá {nome}, com {peso} kgs e {altura}m você tem um iMC de {imc:.2f}'
print(resposta_2)
# outra tentativa
print(f'Olá {nome}, você tem um IMC de: {imc:2f}')
