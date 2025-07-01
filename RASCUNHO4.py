dados = {
    "cliente1": {"nome": "Carlos", "saldo": 1000},
    "cliente2": {"nome": "Ana", "saldo": 2000},
    "notas" : ['Camaronese', 'Beterrabese', 'Amoronese']
}

print(dados["notas"][1])

for nome in dados["notas"]:
    print(nome)
print()
for idc, nome in enumerate(dados["notas"]):
    print(idc, nome)


