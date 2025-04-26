'''
Closure e funções que retornam outras funções

Closures (fechamentos) são um conceito poderoso em Python que permite que
uma função interna "lembre" e acesse variáveis do escopo da função externa mesmo
após a função externa ter terminado sua execução

'''
import sys
# '''
# Tem 2 parâmetros e Retorna os 2 Argumentos informados pelo usuário:
def criar_saudacao(saudacao, nome):
    return f'{saudacao},nobre {nome}!'
# Variável = recebe a função com os argumentos:
s1 = criar_saudacao('Bom dia', 'Zumiro')
# outra Variável = recebendo outro tipo de argumento:
s2 = criar_saudacao('Boa Noite', 'Castro Neves')
print(f'{s1},\n{s2}')
print('===' * 10)
print(f'{criar_saudacao('Olá', 'Azambuja Johnes')}')# sem variáveis

# em abas saídas a função só serve para exibir a palavra 'nobre' e o '!'
# '''

print('*='* 45)

#sys.exit()

def Quero_Saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}\033[1;31;40m,e ai Blz?\033[0m {nome}!'
    return saudar# Ele retorna para a Func Quero_SAudacao
# é uma função que tem um ParÂmentro (de saudação) e chama outra com parametro ( de nome)
# que organiza a saída com a Saudação um Elo e um nome!
print(Quero_Saudacao('Opa!')('ZembraYanovic'))


sys.exit()

falar_bom_dia = Quero_Saudacao('Bom dia, como está você?')
falar_boa_noite = Quero_Saudacao('Boa noite, está cansado?')

for nome in ['Marco', 'Teodoro', 'Toninho']:
    print(falar_bom_dia(nome))#Closer
    print(falar_boa_noite(nome))# Closer

print('===' * 35)
print(falar_bom_dia('Renata'))