'''
Iterable (Lista, Tupla, etc.)        X 	Generator Expression

Armazena todos os dados na memória	X   Gera valores sob demanda (economiza memória)
Pode ser iterado múltiplas vezes    X	Só pode ser iterado uma vez
Sintaxe: [x for x in ...]	        X   Sintaxe: (x for x in ...)

Quando Usar?
Use generator expressions para economizar memória ao trabalhar com grandes 
conjuntos de dados.

Use iterables (como listas) quando precisar acessar os dados várias vezes
ou modificar a estrutura.
'''


#Exemplo Prático:

# Lista (ocupa mais memória)
lista = [x * 2 for x in range(1000000)]  

# Generator (economiza memória)
generator = (x * 2 for x in range(1000000)) 