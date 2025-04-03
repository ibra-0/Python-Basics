import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
SPEED = 5
OBSTACLE_SPEED = 7  
LANE_WIDTH = 200
COIN_SPEED = 5
N = 5  
WIN_SCORE = 10  

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()

player_car = pygame.image.load("player_car.png")
player_car = pygame.transform.scale(player_car, (80, 160))

obstacle_car = pygame.image.load("obstacle_car.png")
obstacle_car = pygame.transform.scale(obstacle_car, (50, 100))

road = pygame.image.load("road.png")
road = pygame.transform.scale(road, (WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 48)
def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

class Player:
    def __init__(self):
        self.rect = player_car.get_rect(center=(WIDTH // 2, HEIGHT - 100))

    def move(self, dx):
        self.rect.x += dx * SPEED
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

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

def main():
    player = Player()
    obstacles = []
    coins = []
    score = 0
    global OBSTACLE_SPEED  
    road_y = 0
    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-1)
        if keys[pygame.K_RIGHT]:
            player.move(1)

        if not game_over:
            if score >= WIN_SCORE:
                screen.fill(GREEN)
                draw_text("You Win!", BLACK, WIDTH // 2 - 100, HEIGHT // 2 - 50)
                pygame.display.flip()
                pygame.time.delay(3000)
                break
            
            road_y += OBSTACLE_SPEED
            if road_y >= HEIGHT:
                road_y = 0

            screen.blit(road, (0, road_y - HEIGHT))
            screen.blit(road, (0, road_y))

            if random.randint(1, 30) == 1:
                obstacles.append(Obstacle())
            if random.randint(1, 50) == 1:
                coins.append(Coin())

            for coin in coins[:]:
                coin.move()
                coin.draw()

                if coin.rect.top > HEIGHT:
                    coins.remove(coin)

                if player.rect.colliderect(coin.rect):
                    score += coin.value 
                    coins.remove(coin)

                    if score % N == 0:
                        OBSTACLE_SPEED += 1

            for obstacle in obstacles[:]:
                obstacle.move()
                obstacle.draw()

                if obstacle.rect.top > HEIGHT:
                    obstacles.remove(obstacle)

                if player.rect.colliderect(obstacle.rect):
                    game_over = True

            player.draw()
            draw_text(f"Score: {score}", BLACK, 10, 10)

        else:
            draw_text("Game Over!", RED, WIDTH // 2 - 150, HEIGHT // 2 - 50)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
