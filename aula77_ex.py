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
'''
p0 = perguntas[0]['Pergunta']
p1 = perguntas[1]['Pergunta']
p2 = perguntas[2]['Pergunta']
op0 = perguntas[0]['Opções']
op1 = perguntas[1]['Opções']
op2 = perguntas[2]['Opções']
'''
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

sys.exit()
emojis = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":rocket:": "🚀",
    ":snake:": "🐍",
    ":computer:": "💻"
}

print("Escolha um emoji:")
'''
for code in emojis:
    print(f"{code} -> {emoji.emojize(code)}")
'''
escolha = ':snake:'
print(f"Você escolheu: {emoji.emojize(escolha)}")

