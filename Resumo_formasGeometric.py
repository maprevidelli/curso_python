## 1. Usando Matplotlib para visualização

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon

# Criar figura
fig, ax = plt.subplots()

# Retângulo
retangulo = Rectangle((1, 1), 3, 2, fill=False, edgecolor='blue')
ax.add_patch(retangulo)

# Círculo
circulo = Circle((5, 3), 1.5, fill=False, edgecolor='red')
ax.add_patch(circulo)

# Triângulo (polígono)
triangulo = Polygon([[3, 5], [4, 7], [5, 5]], closed=True, fill=False, edgecolor='green')
ax.add_patch(triangulo)

# Configurar limites e aspecto
ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
ax.set_aspect('equal')

plt.title('Formas Geométricas com Matplotlib')
plt.grid(True)
plt.show()


## 2. Usando Turtle Graphics para desenho interativo

import turtle

# Configuração inicial
tela = turtle.Screen()
tela.title("Formas Geométricas com Turtle")
caneta = turtle.Turtle()

# Quadrado
for _ in range(4):
    caneta.forward(100)
    caneta.left(90)

# Círculo
caneta.penup()
caneta.goto(150, 0)
caneta.pendown()
caneta.circle(50)

# Triângulo
caneta.penup()
caneta.goto(-150, 0)
caneta.pendown()
for _ in range(3):
    caneta.forward(100)
    caneta.left(120)

turtle.done()


## 3. Usando OpenCV para processamento de imagens

import numpy as np
import cv2

# Criar imagem em branco
img = np.zeros((500, 500, 3), dtype=np.uint8)

# Retângulo
cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0), 2)

# Círculo
cv2.circle(img, (300, 100), 50, (0, 255, 0), 2)

# Polígono (pentágono)
pontos = np.array([[400, 50], [450, 100], [425, 175], [375, 175], [350, 100]])
cv2.polylines(img, [pontos], isClosed=True, color=(0, 0, 255), thickness=2)

# Mostrar imagem
cv2.imshow('Formas Geométricas', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


## 4. Usando Pygame para jogos e aplicações interativas

import pygame

# Inicializar pygame
pygame.init()

# Configurar tela
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Formas Geométricas com Pygame")

# Cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)

# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    
    # Preencher fundo
    tela.fill(BRANCO)
    
    # Desenhar formas
    pygame.draw.rect(tela, AZUL, (50, 50, 100, 80))  # Retângulo
    pygame.draw.circle(tela, VERMELHO, (300, 100), 50)  # Círculo
    pygame.draw.polygon(tela, VERDE, [(450, 50), (500, 150), (400, 150)])  # Triângulo
    
    pygame.display.flip()

pygame.quit()