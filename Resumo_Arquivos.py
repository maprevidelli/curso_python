import sys
# abre um txt na pasta:
file = open('pilotosf1.txt')
print(file.read())
file.close()
# solicita algo para ser escrito no arquivo 'a' append:
with open('pilotosf1.txt', 'a') as file:
    texto = input('Entre com outro piloto: ')
    print(file.write(texto))

sys.exit()

