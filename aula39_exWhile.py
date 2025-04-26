'''
Iterando com Strings e While
'''
nome = 'Marco Antonio'
letras = len(nome)
print(letras)
print(nome[3])
cont = 0
while cont <= letras:
    print(' * ', nome[cont], end="")
    cont += 1
