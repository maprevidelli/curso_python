"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1


def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)# saída: 11 - 4ª saída


print(x)# saída: 1 (Escopo Externo) # 1ª saída
escopo()# saída: 11 2 (Escopo função interna) # 2º saída
print(x)# saída: 11 - 3ª saída