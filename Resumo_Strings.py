# Aula 55
"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)

### Resumo de Strings pela IA

# 2. Acesso a Caracteres por Índices
# Strings são indexadas, o que significa que cada caractere tem um índice numérico, começando do 0.
texto = "Python"
print(texto[0])  # Saída: "P"
print(texto[3])  # Saída: "h"
# indices negativos contam a partir do final:
print(texto[-1])  # Saída: "n" (último caractere)
print(texto[-2])  # Saída: "o" (penúltimo caractere)

# 3. Fatiamento (Slicing)
# Permite extrair substrings usando a sintaxe [início:fim:passo].
texto = "Programação"
print(texto[0:5])   # Saída: "Progr" (do índice 0 ao 4)
print(texto[3:])    # Saída: "gramação" (do índice 3 até o final)
print(texto[:6])    # Saída: "Progra" (do início até o índice 5)
print(texto[::2])   # Saída: "Pormçã" (pula de 2 em 2)
print(texto[::-1])  # Saída: "oãçamargorP" (inverte a string)

# 4. Operações com Strings
# Concatenação: Juntar strings com +.
texto1 = "Olá"
texto2 = "Mundo"
resultado = texto1 + ", " + texto2  # Saída: "Olá, Mundo"
# Repetição: Repetir strings com *
texto = "A"
print(texto * 3)  # Saída: "AAA"
# Verificação de pertinência: Verificar se uma substring está presente com in
print("mun" in "Olá, mundo!")  # Saída: True

# 5. Métodos Úteis de Strings
# Conversão de caixa:
texto = "Python"
print(texto.upper())  # Saída: "PYTHON"
print(texto.lower())  # Saída: "python"
print(texto.title())  # Saída: "Python"
# Remoção de espaços:
texto = "  Olá  "
print(texto.strip())   # Saída: "Olá" (remove espaços no início e fim)
print(texto.lstrip())  # Remove espaços à esquerda
print(texto.rstrip())  # Remove espaços à direita
# Substituição:
texto = "Olá, mundo!"
print(texto.replace("mundo", "Python"))  # Saída: "Olá, Python!"
# Divisão e junção:
texto = "Python é incrível"
print(texto.split())  # Saída: ["Python", "é", "incrível"] (divide por espaços)
print("-".join(["Python", "é", "incrível"]))  # Saída: "Python-é-incrível"
# Busca:
texto = "Olá, mundo!"
print(texto.find("mundo"))  # Saída: 5 (índice onde começa a substring)
print(texto.startswith("Olá"))  # Saída: True
print(texto.endswith("!"))      # Saída: True
# Formatação:
nome = "Maria"
idade = 30
print(f"{nome} tem {idade} anos.")  # Saída: "Maria tem 30 anos."

# 6. Strings são Imutáveis
# Strings não podem ser alteradas após criadas.
#  Qualquer operação que "modifica" uma string cria uma nova string.
texto = "Python"
# texto[0] = "J"  # Isso causaria um erro!
novo_texto = "J" + texto[1:]  # Saída: "Jython"

# 7. Iteração sobre Strings
# É possível iterar sobre cada caractere de uma string usando um loop for.
texto = "Python"
for letra in texto:
    print(letra)

# 8. Funções Úteis com Strings
# len(): Retorna o comprimento da string.
print(len("Python"))  # Saída: 6
# str(): Converte outros tipos de dados em strings.
numero = 42
print(str(numero))  # Saída: "42"

# 9. Strings Multilinha
# Use aspas triplas para strings que ocupam várias linhas.
texto = """Linha 1
Linha 2
Linha 3"""
print(texto)

# 10. Caracteres de Escape
#Alguns caracteres especiais são representados com barras invertidas (\):

# \n: Nova linha

# \t: Tabulação

# \\: Barra invertida

# \": Aspas duplas

# \': Aspas simples
print("Olá\nMundo!")  # Saída: "Olá" na primeira linha e "Mundo!" na segunda.

# 11. Strings Unicode
# Python suporta caracteres Unicode, permitindo o uso de emojis e caracteres especiais.
print("Olá, 🌍!")  # Saída: "Olá, 🌍!"

# 12. Comparação de Strings
# Strings podem ser comparadas com operadores como ==, !=, >, <, etc.
# A comparação é feita com base na ordem lexicográfica (ordem alfabética).
print("abc" == "abc")  # Saída: True
print("abc" < "def")   # Saída: True

# 13. Métodos de Verificação
# isalpha(): Verifica se todos os caracteres são letras.

# isdigit(): Verifica se todos os caracteres são dígitos.

# isalnum(): Verifica se todos os caracteres são alfanuméricos.

# isspace(): Verifica se todos os caracteres são espaços.
print("Python".isalpha())  # Saída: True
print("123".isdigit())     # Saída: True

# 14. Strings e Codificação
# Strings podem ser codificadas em diferentes formatos, como UTF-8, ASCII, etc.
texto = "Olá, mundo!"
print(texto.encode("utf-8"))  # Saída: b'Ol\xc3\xa1, mundo!'