"""
 Operação ternária (condicional de uma linha)
 <valor> if <condicao> else <outro valor>
 """
condicao = 10 == 11 # = Falso
variavel = 'Valor_1' if condicao else 'Outro valor_2'# saída: Outro valor_2
print(variavel)
print('&' * 25)
digito = 9  # > 9 = 0
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('*' * 25)
print('Valor' if False else 'Outro valor' if False else 'Fim')