# Exercício - sistema de perguntas e respostas


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
import emoji

emojis = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":rocket:": "🚀",
    ":snake:": "🐍",
    ":computer:": "💻"
}

print("Escolha um emoji:")
for code in emojis:
    print(f"{code} -> {emoji.emojize(code)}")

escolha = input("Digite o código do emoji: ")
print(f"Você escolheu: {emoji.emojize(escolha)}")

