numeros = [1, 2, 3, 4, 5]

def quadrado(x):
    return x ** 2

# Aplicando map
quadrados = list(map(quadrado, numeros))
print(quadrados)  # Saída: [1, 4, 9, 16, 25]

# Com lambda (função anônima)
quadrados = list(map(lambda x: x**2, numeros))