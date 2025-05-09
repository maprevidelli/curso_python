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

score = 0

for pergunta in perguntas:
    print('\nPergunta:', pergunta['Pergunta'])
    print()
    
    for i, item in enumerate(pergunta['Opções']):
        print(f'{i})', item)
    
    print()
    escolha = input('Escolha uma opção: ')
    
    # Verifica se a escolha está correta
    if escolha == pergunta['Resposta']:
        print('Resposta correta!')
        score += 1
    else:
        print('Resposta incorreta!')

print(f'\nVocê acertou {score} de {len(perguntas)} perguntas.')