"""
For + Range
range -> range(start, stop, step)
"""
#numeros = range(-1, -15, -1)
#numeros = range(2, 15)
#for numero in numeros:
    #print(numero)

###

"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# for letra in texto
texto = 'Python'  # iterável

iteratador = iter(texto)  # iterator
# Transformou uma String "Python" em algo iterável, senão daria erro: 
# TypeError: 'str' object is not an iterator
while True:
     try:
         letra = next(iteratador)
         print(letra)
     except StopIteration:
         print('Entrou em StopIteration')
         break

#for letra in texto:
#   print(letra)    