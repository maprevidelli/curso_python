"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
def limpa_cpf(cpf):
    return cpf.strip().replace('.', '').replace('-', '')

while True:
    cpf = input('\nDigite seu CPF[xxx.xxx.xxx-xx]: ')
    print(f"CPF limpo: {limpa_cpf(cpf)}")
    # armazenar os 2 digitos finais
    digitos_finais = (cpf[-2:])
    print(digitos_finais)
    digitos_9 = (limpa_cpf(cpf)[0:9])
    print(digitos_9)
    if digitos_9.isnumeric() == True and len(digitos_9) == 9:
        #converter as strings em uma lista para iterar depois
        lista_digital = list(digitos_9)
        print(lista_digital)
        # converter para inteiros
        lista = list(map(int, lista_digital))
        # realizar a multiplicação 10 decrescente
        contador = total = 0
        num_reves = 10
        while contador < 9:
            for item in lista:
                total_parcial = item * num_reves
                total += total_parcial
                num_reves -= 1
                contador += 1
                continue
        print('soma de todos resultados = ', total)
        # Multiplicar o resultado por 10
        total = total * 10
        # obter o resto da divisão por 11
        total = total % 11
        print(f'Digito = {total}'if total >= 9 else "Digito_1 = 0")
    else:
        print('\nDigitos inválidos! verifique e tente novamente!')
        continue
# FIZ TUDO ISSO PQ NAO SABIA QUE DAVA PARA ITERAR COM O FOR - IN
# transformei em lista pra poder fazer isso