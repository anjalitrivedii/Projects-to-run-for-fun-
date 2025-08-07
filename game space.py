# import pygame
# import random
#
# pygame.init()
#
# # Screen dimensions
# WIDTH, HEIGHT = 750, 750
# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Simple Space Shooter")
#
# # Colors
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 100, 255)
# YELLOW = (255, 255, 0)
# BLACK = (0, 0, 0)
#
# # Fonts
# main_font = pygame.font.SysFont("comicsans", 40)
# lost_font = pygame.font.SysFont("comicsans", 60)
#
# # Player and laser sizes
# SHIP_WIDTH, SHIP_HEIGHT = 50, 40
# LASER_WIDTH, LASER_HEIGHT = 5, 10
#
# class Laser:
#     def __init__(self, x, y, color):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.rect = pygame.Rect(self.x, self.y, LASER_WIDTH, LASER_HEIGHT)
#
#     def draw(self, window):
#         pygame.draw.rect(window, self.color, self.rect)
#
#     def move(self, vel):
#         self.y += vel
#         self.rect.y = self.y
#
#     def off_screen(self):
#         return not (0 <= self.y <= HEIGHT)
#
#     def collision(self, obj):
#         return self.rect.colliderect(obj.get_rect())
#
#
# class Ship:
#     COOLDOWN = 30
#
#     def __init__(self, x, y, health=100, color=RED):
#         self.x = x
#         self.y = y
#         self.health = health
#         self.color = color
#         self.lasers = []
#         self.cool_down_counter = 0
#
#     def draw(self, window):
#         pygame.draw.rect(window, self.color, self.get_rect())
#         for laser in self.lasers:
#             laser.draw(window)
#
#     def move_lasers(self, vel, objs):
#         self.cooldown()
#         for laser in self.lasers[:]:
#             laser.move(vel)
#             if laser.off_screen():
#                 self.lasers.remove(laser)
#             else:
#                 for obj in objs:
#                     if laser.collision(obj):
#                         objs.remove(obj)
#                         if laser in self.lasers:
#                             self.lasers.remove(laser)
#
#     def cooldown(self):
#         if self.cool_down_counter >= self.COOLDOWN:
#             self.cool_down_counter = 0
#         elif self.cool_down_counter > 0:
#             self.cool_down_counter += 1
#
#     def shoot(self):
#         if self.cool_down_counter == 0:
#             laser = Laser(self.x + SHIP_WIDTH // 2 - 2, self.y, self.color)
#             self.lasers.append(laser)
#             self.cool_down_counter = 1
#
#     def get_rect(self):
#         return pygame.Rect(self.x, self.y, SHIP_WIDTH, SHIP_HEIGHT)
#
#     def get_width(self):
#         return SHIP_WIDTH
#
#     def get_height(self):
#         return SHIP_HEIGHT
#
#
# class Player(Ship):
#     def __init__(self, x, y, health=100):
#         super().__init__(x, y, health, YELLOW)
#         self.max_health = health
#
#     def draw(self, window):
#         super().draw(window)
#         self.healthbar(window)
#
#     def healthbar(self, window):
#         pygame.draw.rect(window, RED, (self.x, self.y + SHIP_HEIGHT + 10, SHIP_WIDTH, 10))
#         pygame.draw.rect(window, GREEN, (self.x, self.y + SHIP_HEIGHT + 10,
#                                          SHIP_WIDTH * (self.health / self.max_health), 10))
#
#
# class Enemy(Ship):
#     def __init__(self, x, y, color, health=100):
#         super().__init__(x, y, health, color)
#
#     def move(self, vel):
#         self.y += vel
#
#     def shoot(self):
#         if self.cool_down_counter == 0:
#             laser = Laser(self.x + SHIP_WIDTH // 2 - 2, self.y + SHIP_HEIGHT, self.color)
#             self.lasers.append(laser)
#             self.cool_down_counter = 1
#
#
# def main():
#     run = True
#     FPS = 60
#     level = 0
#     lives = 5
#
#     enemies = []
#     wave_length = 5
#     enemy_vel = 1
#     laser_vel = 5
#
#     player_vel = 5
#     player = Player(300, 630)
#
#     clock = pygame.time.Clock()
#     lost = False
#     lost_count = 0
#
#     def redraw_window():
#         WIN.fill(BLACK)
#         lives_label = main_font.render(f"Lives: {lives}", 1, WHITE)
#         level_label = main_font.render(f"Level: {level}", 1, WHITE)
#
#         WIN.blit(lives_label, (10, 10))
#         WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
#
#         for enemy in enemies:
#             enemy.draw(WIN)
#
#         player.draw(WIN)
#
#         if lost:
#             lost_label = lost_font.render("GAME OVER", 1, WHITE)
#             WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, HEIGHT / 2))
#
#         pygame.display.update()
#
#     while run:
#         clock.tick(FPS)
#         redraw_window()
#
#         if lives <= 0 or player.health <= 0:
#             lost = True
#             lost_count += 1
#
#         if lost and lost_count > FPS * 3:
#             run = False
#
#         if len(enemies) == 0:
#             level += 1
#             wave_length += 5
#             for _ in range(wave_length):
#                 x = random.randint(50, WIDTH - SHIP_WIDTH - 50)
#                 y = random.randint(-1500, -100)
#                 color = random.choice([RED, BLUE, GREEN])
#                 enemy = Enemy(x, y, color)
#                 enemies.append(enemy)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#
#         # Player input
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_a] and player.x - player_vel > 0:
#             player.x -= player_vel
#         if keys[pygame.K_d] and player.x + player_vel + SHIP_WIDTH < WIDTH:
#             player.x += player_vel
#         if keys[pygame.K_w] and player.y - player_vel > 0:
#             player.y -= player_vel
#         if keys[pygame.K_s] and player.y + player_vel + SHIP_HEIGHT < HEIGHT:
#             player.y += player_vel
#         if keys[pygame.K_SPACE]:
#             player.shoot()
#
#         # Enemy movement
#         for enemy in enemies[:]:
#             enemy.move(enemy_vel)
#             enemy.move_lasers(laser_vel, [player])
#
#             if random.randint(0, 120) == 1:
#                 enemy.shoot()
#
#             if enemy.get_rect().colliderect(player.get_rect()):
#                 player.health -= 10
#                 enemies.remove(enemy)
#             elif enemy.y + SHIP_HEIGHT > HEIGHT:
#                 lives -= 1
#                 enemies.remove(enemy)
#
#         player.move_lasers(-laser_vel, enemies)
#
#
# def main_menu():
#     run = True
#     title_font = pygame.font.SysFont("comicsans", 60)
#     while run:
#         WIN.fill(BLACK)
#         title = title_font.render("Click to Play!", 1, WHITE)
#         WIN.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2))
#         pygame.display.update()
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 main()
#     pygame.quit()
#
#
# main_menu()
import pygame
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Shooter")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
PINK = (255, 0, 100)
BLACK = (0, 0, 0)

# Fonts
main_font = pygame.font.SysFont("comicsans", 40)
lost_font = pygame.font.SysFont("comicsans", 60)

# Sizes
SHIP_WIDTH, SHIP_HEIGHT = 50, 40
LASER_WIDTH, LASER_HEIGHT = 5, 10


class Laser:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, LASER_WIDTH, LASER_HEIGHT)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def move(self, vel):
        self.y += vel
        self.rect.y = self.y

    def off_screen(self):
        return not (0 <= self.y <= HEIGHT)

    def collision(self, obj):
        return self.rect.colliderect(obj.get_rect())


class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100, color=RED):
        self.x = x
        self.y = y
        self.health = health
        self.color = color
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        if isinstance(self, Player):
            # Strawberry shape
            pygame.draw.ellipse(window, PINK, (self.x, self.y, SHIP_WIDTH, SHIP_HEIGHT))  # body
            pygame.draw.polygon(window, GREEN, [  # leaves
                (self.x + SHIP_WIDTH // 2, self.y - 5),
                (self.x + SHIP_WIDTH // 2 - 10, self.y + 5),
                (self.x + SHIP_WIDTH // 2 + 10, self.y + 5)
            ])
        elif isinstance(self, Enemy):
            # Apple shape
            pygame.draw.ellipse(window, self.color, (self.x, self.y, SHIP_WIDTH, SHIP_HEIGHT))  # body
            pygame.draw.rect(window, BROWN, (self.x + SHIP_WIDTH // 2 - 2, self.y - 5, 4, 8))  # stem
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers[:]:
            laser.move(vel)
            if laser.off_screen():
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x + SHIP_WIDTH // 2 - 2, self.y, WHITE)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_rect(self):
        return pygame.Rect(self.x, self.y, SHIP_WIDTH, SHIP_HEIGHT)


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health, PINK)
        self.max_health = health

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, RED, (self.x, self.y + SHIP_HEIGHT + 10, SHIP_WIDTH, 10))
        pygame.draw.rect(window, GREEN, (self.x, self.y + SHIP_HEIGHT + 10,
                                         SHIP_WIDTH * (self.health / self.max_health), 10))


class Enemy(Ship):
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health, color)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x + SHIP_WIDTH // 2 - 2, self.y + SHIP_HEIGHT, WHITE)
            self.lasers.append(laser)
            self.cool_down_counter = 1


def main():
    run = True
    FPS = 60
    level = 0
    lives = 5

    enemies = []
    wave_length = 5
    enemy_vel = 1
    laser_vel = 5

    player_vel = 5
    player = Player(300, 630)

    clock = pygame.time.Clock()
    lost = False
    lost_count = 0

    def redraw_window():
        WIN.fill(BLACK)
        lives_label = main_font.render(f"Lives: {lives}", 1, WHITE)
        level_label = main_font.render(f"Level: {level}", 1, WHITE)

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("GAME OVER", 1, WHITE)
            WIN.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, HEIGHT / 2))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost and lost_count > FPS * 3:
            run = False

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for _ in range(wave_length):
                x = random.randint(50, WIDTH - SHIP_WIDTH - 50)
                y = random.randint(-1500, -100)
                color = random.choice([RED, GREEN])
                enemy = Enemy(x, y, color)
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + SHIP_WIDTH < WIDTH:
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + SHIP_HEIGHT < HEIGHT:
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        # Enemy movement
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, [player])

            if random.randint(0, 120) == 1:
                enemy.shoot()

            if enemy.get_rect().colliderect(player.get_rect()):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + SHIP_HEIGHT > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)


def main_menu():
    run = True
    title_font = pygame.font.SysFont("comicsans", 60)
    while run:
        WIN.fill(BLACK)
        title = title_font.render("Click to Play!", 1, WHITE)
        WIN.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()
