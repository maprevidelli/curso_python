# 1ª parte - verificador de 1º digito de CPF
import re
cpf = input('Digite o CPF (somente números/ sem digitos finais): ')
# para limpar . e - do cpf além de outras coisas pode ser feito como fiz 
# no codigo anterior ou essa maneira onde importamos o re - ^ = não --> 
# o que nâo for de 0-9
cpf_enviado = re.sub(r'[^0-9]', '', cpf)
print(f'CPF digitado {cpf}\n CPF mexido pelo RE = {cpf_enviado}')

nove_digitos = cpf[:9]
numero_regressivo = 10
total_primeiro = 0
for digito_inicial in nove_digitos:
    total_primeiro += int(digito_inicial) * numero_regressivo
    numero_regressivo -= 1
primeiro_digito = (total_primeiro * 10) % 11

print(f'Primeiro Digito = {primeiro_digito}' if primeiro_digito <= 9 else
      'Primeiro Digito = 0')

if primeiro_digito > 9:
    primeiro_digito = 0
print('=== primeiro digito --> ', primeiro_digito)  
total_primeiro = digito_inicial = 0
numero_regressivo = 11
# 2ª parte - verificador do 2º digito de CPF
dez_digitos = cpf + str(primeiro_digito)
print(dez_digitos)
for digito_inicial in dez_digitos:
    total_primeiro += int(digito_inicial) * numero_regressivo
    numero_regressivo -= 1
segundo_digito = (total_primeiro * 10) % 11

if segundo_digito > 9:
    segundo_digito = 0
print('=== segundo digito --> ', segundo_digito)    
