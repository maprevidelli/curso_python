nome_str = ('Olá Mundo')
print(f'{nome_str}')
print(len(nome_str))

digitado = input('Entre com um número: ') # digite uma letra
digitado = int(digitado)
try:
    if digitado >= 1:
        print('Parabéns!')
    else: 
        print('Não deu')    
except:
    print('Isso não é um número!')        
