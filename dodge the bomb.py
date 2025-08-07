import pygame
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("💣 Dodge the Bomb")

# Colors
WHITE = (255, 255, 255)
RED = (220, 20, 60)
BLUE = (0, 120, 255)
BLACK = (0, 0, 0)

# Player settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 20
player_x = WIDTH // 2 - PLAYER_WIDTH // 2
player_y = HEIGHT - 60
player_vel = 8

# Bomb settings
bomb_radius = 20
bombs = []
bomb_speed = 5
spawn_rate = 25  # lower = more frequent

# Score
score = 0
font = pygame.font.SysFont("comicsans", 40)

clock = pygame.time.Clock()
run = True


def draw_window():
    WIN.fill(BLACK)

    # Draw player
    pygame.draw.rect(WIN, BLUE, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    # Draw bombs
    for bomb in bombs:
        pygame.draw.circle(WIN, RED, (bomb[0], bomb[1]), bomb_radius)

    # Score
    score_text = font.render(f"Score: {score}", 1, WHITE)
    WIN.blit(score_text, (10, 10))

    pygame.display.update()


while run:
    clock.tick(60)
    draw_window()
    score += 1

    # Event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_vel > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x + player_vel + PLAYER_WIDTH < WIDTH:
        player_x += player_vel

    # Spawn bombs
    if random.randint(1, spawn_rate) == 1:
        bomb_x = random.randint(bomb_radius, WIDTH - bomb_radius)
        bombs.append([bomb_x, -bomb_radius])

    # Move bombs
    for bomb in bombs[:]:
        bomb[1] += bomb_speed
        if bomb[1] > HEIGHT:
            bombs.remove(bomb)

        # Collision check
        player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
        bomb_rect = pygame.Rect(bomb[0] - bomb_radius, bomb[1] - bomb_radius, bomb_radius * 2, bomb_radius * 2)
        if player_rect.colliderect(bomb_rect):
            run = False  # Game Over

# Game Over screen
WIN.fill(BLACK)
game_over_text = font.render("💥 GAME OVER 💥", 1, WHITE)
final_score_text = font.render(f"Final Score: {score}", 1, WHITE)
WIN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 40))
WIN.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2 + 10))
pygame.display.update()
pygame.time.delay(3000)

pygame
