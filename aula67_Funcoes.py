#
"""
 Valores padrão para parâmetros
 Ao definir uma função, os parâmetros podem
 ter valores padrão. Caso o valor não seja
 enviado para o parâmetro, o valor padrão será
 usado.
 Refatorar: editar o seu código.
 """ 
 
 # Z = none - seria a mesma coisa que definir anteriormente
 
def soma(x, y, z=None):
     if z is not None:# Se Z não for None = Se Z foi argumentado, faça isso:
         print(f'{x=} {y=} {z=}', x + y + z)
     else:# Caso não foi informado/argumentado, faça:
         print(f'{x=} {y=}', x + y)
 
 
soma(1, 2)
soma(3, 5)
soma(100, 200)
print('Z informado: ')
soma(7, 9, 0)
print('Z informado: ')
soma(y=9, z=0, x=7)