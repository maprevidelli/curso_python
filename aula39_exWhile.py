'''
Iterando com Strings e While
'''
nome = 'Marco Antonio Previdelli'

# tratar a variavel - Input
espaco  = nome.count(' ')
letras = len(nome) - espaco
print(letras)
print(nome[3])
cont = 0
while cont <= letras + 1:
    print(' * ', nome[cont], end="")
    cont += 1
print()    
