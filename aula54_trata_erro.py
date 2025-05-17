"""
Faça uma Lista de compras com listas;
usuário tem a possibilidade de:
inserir, apagar e listar os valores na lista
e não é permitido que o programa quebre com erros de índices inexistenstes na lista
"""
import os  

lista = []
while True:
    print('=' * 10)
    print('I. Inserir\nA. Apagar\nL. Listar\n')
    opcao = input('Entre com a opção: ').lower()
    print('=' * 10)
    opcao_valida = ['i', 'a', 'l']# limitei somente ás opçoes
    if opcao not in  opcao_valida:
        print('Erro: opção inválida seu Animal')
        continue# porém volta para o ciclo
    if opcao == 'l':
            os.system('clear')
            for indice, nome in enumerate(lista):#Lista o indice e o item da Lista
                print(indice, nome)
                continue
            if len(lista) == 0:# se a lista estiver vazia
                print('>>>> Não há nada na lista ainda <<<<')    
            continue

    if opcao == 'i':  
        os.system('clear') # Limpa a tela para começar a digitar
        nome = input('Entre com um valor: ')
        lista.append(nome)
        continue
    if opcao == 'a':
        try:
            item = int(input('Digite o numero do item a ser apagado: '))
            del lista[item]
            continue
        except IndexError:# pega o erro e isere aqui para tratar expecifico
             print('>>> Indice não consta na lista <<<')
        except ValueError:
             print('>>>> Erro de digitação <<<<')
        #except - poderia ter outros se necessário
