# Exercício - sistema de perguntas e respostas
import sys
import emoji
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

i = 1
score = 0
print(perguntas[0]['Pergunta'])
while i < 4:
    for op in perguntas[0]['Opções']:
        print(f'{i}) {op}')
        i += 1
chose = int(input('Digite a sua opção: '))
if chose == 3:
    print(f'Acertou! 👍')
    score += 1
else:
    print('Errou! ❌')
i = 1
print()
print(perguntas[1]['Pergunta'])
for op in perguntas[1]['Opções']:
        print(f'{i}) {op}')
        i += 1
chose = int(input('Digite a sua opção: '))
if chose == 1:
    print(f'Acertou! 👍')
    score += 1
else:
    print('Errou! ❌')
i = 1    
print()
print(perguntas[2]['Pergunta'])
for op in perguntas[2]['Opções']:
        print(f'{i}) {op}')
        i += 1
chose = int(input('Digite a sua opção: '))
if chose == 2:
    print(f'Acertou! 👍')
    score += 1
else:
    print('Errou! ❌')

print(f'Você acertou {score} de 3 alternativas\nObrigado!\n🐍')
 
# Resposta do Professor:
sys.exc_info()
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')



