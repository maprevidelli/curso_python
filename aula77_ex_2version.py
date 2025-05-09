import sys
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
    print('\nPergunta:', pergunta['Pergunta'])# ITEROU cada pergunta, separada
    print()
    for i, item in enumerate(pergunta['Opções']):# Enumerou a sublista + Iterou "i" p cada item "item"
        print(f'{i})', item)
    print()
    escolha_idx = int(input('Escolha uma opção: '))# vai sair como Str na Lista é Int - temos que igualar

    opcao_escolhida = pergunta['Opções'][escolha_idx]
    print(opcao_escolhida)

    if pergunta['Resposta'] == opcao_escolhida:
        score += 1
        print('Acertou! 👍')
    else:
        print('Errou! ❌')

print(f'\nVocê acertou {score} de 3 questões!')
print()
print('Powered by maprevidelli - PyDev - 🐍')