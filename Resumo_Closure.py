import sys

# Exemplo 01
def externa():
    mensagem = "Olá"  # Variável local da função externa / Ela nao printa
    
    def interna():
        print(mensagem)  # A função interna acessa a variável da externa / faz a ação de Printar
    
    return interna  # Retorna a função interna (sem executá-la) / retirando-se os ()

minha_funcao = externa()  # Agora 'minha_funcao' é a função interna
minha_funcao()  # Saída: Olá

# o que era uma váriável (minha_funcao), passa a ser uma Função ao usar o ()
# REPARE que para enCLAUSURE ela no Return (linha 7) os () são retirados.

'''
Características importantes:
Memória do estado: O closure mantém o estado mesmo após a função externa ter
terminado

Acesso a variáveis não globais: Permite acessar variáveis que não estão no
escopo global

Encapsulamento: Podemos esconder dados em um closure


'''
print('='* 30)
# Exemplo 02

def criar_contador():
    contador = 0  # Estado preservado no closure
    
    def incrementar():
        nonlocal contador  # Permite modificar a variável da função externa
        contador += 1
        return contador
    
    return incrementar

contador1 = criar_contador()
print(contador1())  # 1
print(contador1())  # 2
print(contador1())  # 3

contador2 = criar_contador()
print(contador2())  # 1 (novo closure, novo estado)

print('='*30)
print(contador1())  # 4 (como manteve em memória)

# Eu fiz:
def nome_ext(nome):
    def message_int(msg):
        return f"{nome}: Você está designado para a área específica > {msg}\n Obrigado!"
    return message_int

lista_nomes = ['Marco', 'Teodoro', 'Renata']
setor = 'TI'
for nome in lista_nomes:
    msg_1 = nome_ext(nome)
    print(msg_1(setor))# tive de passar argumento

sys.exit()

# Para não passar argumento:

def nome_ext(nome):
    def message_int():
        return f"{nome}: Você está designado para a área específica > TI\n Obrigado!"
    return message_int

lista_nomes = ['Marco', 'Teodoro', 'Renata']
for nome in lista_nomes:
    msg_1 = nome_ext(nome)
    print(msg_1())  # Agora não precisa passar argumento