import os
# Adivinhar a palavra secreta
secreta = 'python'

# lista para armazenar as letras reveladas
revelada = ['_'] * len(secreta) # Ele conta as letras em "secreta" e aplica em uma lista
# com '_' na mesma quantidade

# Loop - até que contenha '_' na lista ele continua o processo
while '_' in revelada:
    # Exibe a palavra revelada até o momento
    print("Palavra revelada:", " ".join(revelada))
    # Solicita a letra
    letra = input('Digite uma letra: ').lower()
    # verificação se consta na palavra secreta
    if letra in secreta:
        for i, letras in enumerate(secreta):
            if letras == letra:
                revelada[i] = letra # a letra digitada entra no indice do acerto
        print("Letra correta!")
    else:
        print("Letra incorreta. Tente novamente!")
os.system('clear')
print("Parabéns! Você advinou a palavra secreta:", secreta)

# Versão do Professor

"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0