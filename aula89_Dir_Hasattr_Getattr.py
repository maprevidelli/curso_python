# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)


'''
Função	Uso
dir()	Lista atributos/métodos de um objeto.
hasattr()	Verifica se um atributo/método existe.
getattr()	Obtém o valor de um atributo/método.


Essas funções são poderosas para escrever código flexível e genérico, especialmente
em bibliotecas ou frameworks.

'''