'''
Higher Order Functions - Funções de primeira classe

Funções que podem receber e/ou retornar outras funções!

!=

First-Class Functions - Funções que são tratadas como outros tipos de 
dados comuns (strings, inteiros, etc...)


'''

def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)

# Minhas auto-explicações:
print('===' * 30)
# uso simples da FUNCAO 'saudacao' - formada por uma msg e um nome:
print(saudacao('Olá', 'Marco Antonio'))# saída: Olá, Marco Antonio
# a FUNCAO 'executa' têm como parâmentros(uma função, *args e argumentos empacotados)
print(executa(saudacao,'Oi', 'Renata'), 'Tudo bem?', 'Como vai vc?')
# note que ao usar a 'executa' ela aciona a 'saudacao' e volta para para ela *args, depois é fechada
# A FUNCAO 'executa' engloba a FUNCAO 'saudacao'
print