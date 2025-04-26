"""
Lista de Listas e seus índices
"""
salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)],
]
print(salas[0][1])# Saída: Helena
print(salas[2][2])# Saída: Eduarda
print(salas[2][3][2])# Saída: 20

print('==' * 40)

for sala in salas:# laço externo - onde 'sala' define os intens inclusos nessa lista
    print(f'a sala é {sala}')
    for aluno in sala:# 1º laço interno - onde 'aluno' define seus itens internos
        print(aluno)
