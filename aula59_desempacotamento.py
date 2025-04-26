# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

p, b, *_, ap, u = lista
print(p, u, ap) #Saída: Maria Eduarda 3
print(*_) # Saída: 1

print(' === ' * 20)

print('Maria', 'Helena', 1, 2, 3, 'Eduarda')# Saída: Maria Helena 1 2 3 Eduarda
print(*lista) # Saída: Maria Helena 1 2 3 Eduarda
print(*string) # Saíada: A B C D
print(*tupla) # Saída: Python é legal
# equivalem a: for nome in lista: \n print(lista)
# vai passar item a item da lista como o for
print(' =+= ' * 20)
print(*salas, sep='\n')# *Lita = desempacotou sep='\n' = colocou lista interna em uma linha
print(' = - = ' * 20)
print(*salas, end='\n')# colocou cada item em sequência
