nome = input('Digite seu nome: ')
idade = input('Digite sua idade:')
nome_len = (len(nome))
idade = int(idade)
if nome_len and idade >= 1: # if nome and idade: 
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    print(f'Seu nome contém ou não espaços: {' 'in nome}')
    print(f'Seu nome tem {(nome_len) - (nome.count(' '))} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    print(f'Desculpe, você deixou campos vazios.')  

# if nome and idade: 
# simples assim ele já avaliaria de forma booleanda a veracidade se foi ou nao digitado algos