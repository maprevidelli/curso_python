# Tipo Tupla - é uma lista imutável
# Sem os colchetes - 'sem nada' ou (entre parentes)
nomes = 'Maria', 'Joãozinho', 'Luizinho'
nomes_tupla = tuple(nomes)
print(nomes) # Saída: ('Maria', 'Joãozinho', 'Luizinho')
print(nomes_tupla) # Saída: ('Maria', 'Joãozinho', 'Luizinho')
# converter para lista
lista = list(nomes_tupla)
print(f'Forma Lista =======>>>> {lista}') # Saída: ['Maria', 'Joãozinho', 'Luizinho']


