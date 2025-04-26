
#Faça um programa que peça ao usuário para digitar um número inteiro,
#informe se este número é par ou ímpar. Caso o usuário não digite um número
#inteiro, informe que não é um número inteiro.
'''
numero = input(f'Digite um número inteiro: ')
try:
    numero = int(numero)
    if numero % 2 == 0:
        print('Número é par!')
    else:
        print('Número é ímpar!')
except:
    print('Este não é um número inteiro!')   
'''         

'''
numero = input(f'Digite um número inteiro: ')
if numero.lstrip('-').isdigit(): # retira o - pra nao atrapalhar o isdigit que só lê numeros
    numero = int(numero)
    if int(numero % 2) == 1:
        print('Número Ìmpar!')
    else:
        print('Número par')        
else:
    print('Numero nao inteiro')        
'''
      
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
'''
entrada = input('Digite que horas são (0 a 23h): ')

try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora > 11 and hora < 18:
        print('Boa Tarde!')
    elif hora > 17 and hora < 24:
        print('Boa noite!')
    else:
        print('Você digitou algo errado!')
except:
    print("Isso não é um valor para horas")        
'''
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""


nome = input('Qual seu primeiro nome?: ')
print(nome.isalpha)
'''
try:
    letras = len(nome)
    if letras <= 4:
        print('Nome CUrto!')
    elif letras > 4 and letras < 7:
        print('Nome tem um tamanho normal!')
    elif letras > 8:
        print('Seu nome é muuuuuuito grande!')    
except:
    print(f'Desculpe meu amigo mas se teu pai lhe deu {nome} como nome \nEle é um FDP!')
'''