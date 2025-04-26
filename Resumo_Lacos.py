'''
1. Laço for
O laço for é usado para iterar sobre elementos de uma sequência 
(lista, tupla, string, etc.) ou outros objetos iteráveis.
'''
# Iterando sobre uma lista
frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)
# Saída: maçã, banana, laranja (cada uma em uma linha)

# Iterando sobre uma string
for letra in "Python":
    print(letra)
# Saída: P, y, t, h, o, n (cada uma em uma linha)

# Usando range()
for i in range(5):  # 0 a 4
    print(i)
# Saída: 0, 1, 2, 3, 4

for i in range(2, 6):  # 2 a 5
    print(i)
# Saída: 2, 3, 4, 5

for i in range(0, 10, 2):  # 0 a 8, pulando de 2 em 2
    print(i)
# Saída: 0, 2, 4, 6, 8

'''
2. Laço while
O laço while executa um bloco de código enquanto uma condição for verdadeira.
'''
# Contador básico
contador = 0
while contador < 5:
    print(contador)
    contador += 1
# Saída: 0, 1, 2, 3, 4

# Loop até condição ser atendida
senha = ""
while senha != "python123":
    senha = input("Digite a senha: ")
print("Acesso concedido!")

# Loop infinito (com break)
while True:
    comando = input("Digite 'sair' para terminar: ")
    if comando == 'sair':
        break
    print("Você digitou:", comando)

'''
3. Controle de Fluxo em Laços
Python oferece palavras-chave para controlar a execução dos laços:

break - Interrompe o laço completamente
'''    

for num in range(10):
    if num == 5:
        break
    print(num)
# Saída: 0, 1, 2, 3, 4

# continue - Pula para a próxima iteração
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)
# Saída: 1, 3, 5, 7, 9 (apenas ímpares)

# else em Laços - Executa quando o laço termina normalmente (sem break)
for num in range(3):
    print(num)
else:
    print("Laço concluído!")
# Saída: 0, 1, 2, Laço concluído!

for num in range(3):
    if num == 1:
        break
    print(num)
else:
    print("Laço concluído!")
# Saída: 0 (o else não é executado por causa do break)

'''
4. Laços Aninhados
É possível colocar um laço dentro de outro:
'''
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
# Saída: 
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1

'''
5. Laço com enumerate()
Útil quando você precisa do índice e do valor:
'''
frutas = ['maçã', 'banana', 'laranja']
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")
# Saída:
# Índice 0: maçã
# Índice 1: banana
# Índice 2: laranja

'''
6. Laço com zip()
Itera sobre múltiplas sequências simultaneamente:
'''
nomes = ['Ana', 'João', 'Maria']
idades = [25, 30, 28]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")
# Saída:
# Ana tem 25 anos
# Joao tem 30 anos
# Maria tem 28 anos

