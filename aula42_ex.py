# Saber que letra apareceu mais na frase
frase = 'O Python é uma linguagem de programação ' \
    'multiplataforma. ' \
   'Python foi criado por Guido van Rossum.'
#frase = input('Digite uma frase:')
frase = frase.lower() # para tirar maiusculas
print('SEM MAIUSCULAS:',frase)
print('Contar =', len(frase))
frase = frase.strip()
print('Sem espaços fora:', frase)
## essa parte retira-se os espaços e junta a frase em uma coisa só
frase = (frase.split())
frase = ''.join(frase)
print('SEM ESPAÇOS: ', frase)
##
i = 0
maior_apareceu = 1
letra_1 = ''
while i < len(frase):# a partir do indice i=0 começa a contagem das letras na frase
    letra_atual = frase[i]# guarda na variavel a letra em analise
    cont_letra_atual = frase.count(letra_atual)# guarda um valor (int) das aparições da letra
    if cont_letra_atual > maior_apareceu:# estipulei um mínimo (2 vezes) para começar a armazená-la
        maior_apareceu = cont_letra_atual# aqui ele subtitui a quantia maior armazenada caso apareça
        letra_1 = letra_atual# aqui ele armazena a Letra 
    i += 1
print(f'A Letra > {letra_1}\n é a que aparece mais vezes = {maior_apareceu}')
