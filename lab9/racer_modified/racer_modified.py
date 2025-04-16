import pygame
import random
import sys  # Добавлено для корректного выхода

pygame.init()

# Константы
WIDTH, HEIGHT = 800, 500
FPS = 60
SPEED = 5
OBSTACLE_SPEED = 7  
LANE_WIDTH = 200
COIN_SPEED = 5
N = 5  
WIN_SCORE = 10  
MAX_SPEED = 15  # Максимальная скорость препятствий

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)

# Инициализация экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()

# Загрузка изображений с обработкой ошибок
try:
    player_car = pygame.image.load("player_car.png")
    player_car = pygame.transform.scale(player_car, (80, 160))
except:
    player_car = pygame.Surface((80, 160))
    player_car.fill(GREEN)

try:
    obstacle_car = pygame.image.load("obstacle_car.png")
    obstacle_car = pygame.transform.scale(obstacle_car, (50, 100))
except:
    obstacle_car = pygame.Surface((50, 100))
    obstacle_car.fill(RED)

try:
    road = pygame.image.load("road.png")
    road = pygame.transform.scale(road, (WIDTH, HEIGHT))
except:
    road = pygame.Surface((WIDTH, HEIGHT))
    road.fill(BLACK)

# Шрифт
font = pygame.font.SysFont(None, 48)

def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

class Player:
    def __init__(self):
        self.rect = player_car.get_rect(center=(WIDTH // 2, HEIGHT - 100))

    def move(self, dx):
        self.rect.x += dx * SPEED
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))

    def draw(self):
        screen.blit(player_car, self.rect)

class Obstacle:
    def __init__(self):
        self.rect = obstacle_car.get_rect(
            center=(random.choice([WIDTH // 2 - LANE_WIDTH // 2, WIDTH // 2 + LANE_WIDTH // 2]), -100)
        )

    def move(self):
        self.rect.y += OBSTACLE_SPEED 

    def draw(self):
        screen.blit(obstacle_car, self.rect)

class Coin:
    def __init__(self):
        self.value = random.choice([1, 3])  
        self.color = GOLD if self.value == 1 else SILVER 
        self.rect = pygame.Rect(
            random.choice([WIDTH // 2 - LANE_WIDTH // 2, WIDTH // 2 + LANE_WIDTH // 2]), -100, 30, 30
        )

    def move(self):
        self.rect.y += COIN_SPEED

    def draw(self):
        pygame.draw.ellipse(screen, self.color, self.rect)

def show_message(message, color):
    screen.fill(WHITE)
    draw_text(message, color, WIDTH // 2 - 150, HEIGHT // 2 - 50)
    draw_text("Press R to restart or Q to quit", BLACK, WIDTH // 2 - 200, HEIGHT // 2 + 20)
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                    return True  # Рестарт
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
    return False

def main():
    global OBSTACLE_SPEED
    
    player = Player()
    obstacles = []
    coins = []
    score = 0
    OBSTACLE_SPEED = 7  # Сброс скорости
    road_y = 0
    running = True  # Инициализация переменной running
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if not game_over:
            if keys[pygame.K_LEFT]:
                player.move(-1)
            if keys[pygame.K_RIGHT]:
                player.move(1)

            # Движение дороги
            road_y += OBSTACLE_SPEED
            if road_y >= HEIGHT:
                road_y = 0

            # Отрисовка
            screen.blit(road, (0, road_y - HEIGHT))
            screen.blit(road, (0, road_y))

            # Генерация объектов
            if random.randint(1, 30) == 1:
                obstacles.append(Obstacle())
            if random.randint(1, 50) == 1:
                coins.append(Coin())

            # Обновление монет
            for coin in coins[:]:
                coin.move()
                coin.draw()

                if coin.rect.top > HEIGHT:
                    coins.remove(coin)
                elif player.rect.colliderect(coin.rect):
                    score += coin.value 
                    coins.remove(coin)
                    if score % N == 0 and OBSTACLE_SPEED < MAX_SPEED:
                        OBSTACLE_SPEED += 1

            # Обновление препятствий
            for obstacle in obstacles[:]:
                obstacle.move()
                obstacle.draw()

                if obstacle.rect.top > HEIGHT:
                    obstacles.remove(obstacle)
                elif player.rect.colliderect(obstacle.rect):
                    game_over = True

            player.draw()
            draw_text(f"Score: {score}", BLACK, 10, 10)

            # Проверка победы
            if score >= WIN_SCORE:
                if show_message("You Win!", GREEN):
                    return main()  # Рестарт после победы
                else:
                    running = False

        else:
            if show_message("Game Over!", RED):
                return main()  # Рестарт после проигрыша
            else:
                running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()