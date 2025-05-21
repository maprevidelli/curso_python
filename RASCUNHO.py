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