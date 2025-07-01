import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("River Raid Python")

# Cores
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Jogador (avião)
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 100
        self.speed = 5
        self.width = 40
        self.height = 30
        self.bullets = []
        self.score = 0
        self.fuel = 1000
        self.game_over = False

    def draw(self):
        pygame.draw.polygon(screen, WHITE, [
            (self.x, self.y),
            (self.x - self.width//2, self.y + self.height),
            (self.x + self.width//2, self.y + self.height)
        ])
        
        # Desenha balas
        for bullet in self.bullets:
            pygame.draw.rect(screen, RED, (bullet[0], bullet[1], 5, 10))

    def move(self, direction):
        if direction == "left" and self.x > self.width//2:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - self.width//2:
            self.x += self.speed
        if direction == "up" and self.y > 0:
            self.y -= self.speed
        if direction == "down" and self.y < HEIGHT - self.height:
            self.y += self.speed

    def shoot(self):
        self.bullets.append([self.x, self.y])

    def update_bullets(self):
        for bullet in self.bullets[:]:
            bullet[1] -= 10
            if bullet[1] < 0:
                self.bullets.remove(bullet)

# Inimigos
class Enemy:
    def __init__(self):
        self.width = random.randint(30, 60)
        self.height = random.randint(20, 40)
        self.x = random.randint(0, WIDTH - self.width)
        self.y = -self.height
        self.speed = random.randint(2, 5)
        self.type = random.choice(["boat", "helicopter"])
        
    def draw(self):
        if self.type == "boat":
            pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
    
    def move(self):
        self.y += self.speed

# Rio (cenário)
class River:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.scroll_y = 0
        self.speed = 2
        
    def draw(self):
        # Desenha o rio (faixa azul no meio)
        pygame.draw.rect(screen, BLUE, (WIDTH//4, self.scroll_y % HEIGHT, WIDTH//2, HEIGHT))
        pygame.draw.rect(screen, BLUE, (WIDTH//4, (self.scroll_y % HEIGHT) - HEIGHT, WIDTH//2, HEIGHT))
        
    def update(self):
        self.scroll_y += self.speed

# Função principal do jogo
def game():
    clock = pygame.time.Clock()
    player = Player()
    river = River()
    enemies = []
    enemy_spawn_timer = 0
    
    font = pygame.font.SysFont(None, 36)
    
    running = True
    while running:
        clock.tick(60)
        
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
                if event.key == pygame.K_r and player.game_over:
                    player = Player()
                    river = River()
                    enemies = []
        
        if not player.game_over:
            # Movimento do jogador
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move("left")
            if keys[pygame.K_RIGHT]:
                player.move("right")
            if keys[pygame.K_UP]:
                player.move("up")
            if keys[pygame.K_DOWN]:
                player.move("down")
            
            # Atualizações
            player.update_bullets()
            river.update()
            player.fuel -= 0.1
            
            # Spawn de inimigos
            enemy_spawn_timer += 1
            if enemy_spawn_timer >= 60:
                enemies.append(Enemy())
                enemy_spawn_timer = 0
            
            # Movimento e colisão de inimigos
            for enemy in enemies[:]:
                enemy.move()
                
                # Verifica colisão com balas
                for bullet in player.bullets[:]:
                    if (enemy.x < bullet[0] < enemy.x + enemy.width and
                        enemy.y < bullet[1] < enemy.y + enemy.height):
                        player.bullets.remove(bullet)
                        enemies.remove(enemy)
                        player.score += 10
                        break
                
                # Verifica colisão com jogador
                if (player.x - player.width//2 < enemy.x + enemy.width and
                    player.x + player.width//2 > enemy.x and
                    player.y < enemy.y + enemy.height and
                    player.y + player.height > enemy.y):
                    player.game_over = True
                
                # Remove inimigos que saíram da tela
                if enemy.y > HEIGHT:
                    enemies.remove(enemy)
            
            # Verifica se o combustível acabou
            if player.fuel <= 0:
                player.game_over = True
        
        # Desenho
        screen.fill(BLACK)
        river.draw()
        player.draw()
        for enemy in enemies:
            enemy.draw()
        
        # HUD
        score_text = font.render(f"Pontuação: {player.score}", True, WHITE)
        fuel_text = font.render(f"Combustível: {int(player.fuel)}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(fuel_text, (10, 50))
        
        if player.game_over:
            game_over_text = font.render("GAME OVER - Pressione R para reiniciar", True, WHITE)
            screen.blit(game_over_text, (WIDTH//2 - 200, HEIGHT//2))
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game()