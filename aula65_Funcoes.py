# Funções
# Funções podem usar parâmetros para receber valores. 
# Parâmetro é o nome da "variável" dentro dos parênteses, 
# argumento é o valor passado para o parâmetro no momento da execução da função.


def imprimir(a, b, c): # a, b, c  - Parâmetros -> recebem Argumentos
    print('Várias1')
    print('Várias2')
    print('Várias3')
    print('Várias4')

imprimir(1, 2, 3)


def imprimir(a, b, c): # a, b, c  - Parâmetros -> recebem Argumentos
   print(a, b, c) # usando os valores

imprimir(1, 2, 3)
imprimir('d', 'e', 'f')

def saudacao(nome='sem nome'):
    print(f'Olá, {nome}')

saudacao('Marco')# saída: Olá, Marco
saudacao()# saída: Olá, sem nome
# Caso no parametros estivesse: def saudacao(nome):
#saída: TypeError: saudacao() missing 1 required positional argument: 'nome'
# pois faz necessária a entrada de argumentos, e nao foi: saudacao()
