lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def sub_listas(lista, numero):
    sublista = lista[numero]
    
    def repeteco():
        numeros_vistos = set()
        primeiro_repetido = None
        repetidos = set()
        
        for num in sublista:
            if num in numeros_vistos:
                if primeiro_repetido is None:
                    primeiro_repetido = num
                repetidos.add(num)
            else:
                numeros_vistos.add(num)
        
        if not repetidos:
            print('Não há repetições nessa lista!')
        else:
            print(f'Primeiro número a se repetir: {primeiro_repetido}')
            print(f'Números que se repetem: {repetidos}')
    
    return repeteco

# Para usar:
funcao_analise = sub_listas(lista_de_listas_de_inteiros, 1)  # Analisa a segunda sublista
funcao_analise()  # Chama a função de análise