import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Направления
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Класс змейки
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = RIGHT
        self.growing = 0  # Количество клеток для роста

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0] * CELL_SIZE, head_y + self.direction[1] * CELL_SIZE)

        # Проверка на столкновение со стенами или самой собой
        if new_head in self.body or new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= WIDTH or new_head[1] >= HEIGHT:
            return False

        self.body.insert(0, new_head)

        if self.growing > 0:
            self.growing -= 1
        else:
            self.body.pop()

        return True

    def grow(self, amount):
        self.growing += amount

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

# Класс еды
class Food:
    def __init__(self):
        self.spawn()

    def spawn(self):
        while True:
            self.position = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                             random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
            self.weight = random.choice([1, 2, 3])  # Случайный "вес" еды
            self.color = RED if self.weight == 1 else BLUE if self.weight == 2 else YELLOW
            self.timer = random.randint(30, 50)  # Таймер исчезновения еды (в тактах игры)
            if self.position not in snake.body:  # Проверка, чтобы еда не появилась на змейке
                break

    def update(self):
        self.timer -= 1
        if self.timer <= 0:
            self.spawn()

    def draw(self):
        pygame.draw.rect(screen, self.color, (*self.position, CELL_SIZE, CELL_SIZE))

# Основная функция игры
def main():
    global snake
    snake = Snake()
    food = Food()
    running = True

    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Управление змейкой
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and snake.direction != DOWN:
            snake.direction = UP
        if keys[pygame.K_DOWN] and snake.direction != UP:
            snake.direction = DOWN
        if keys[pygame.K_LEFT] and snake.direction != RIGHT:
            snake.direction = LEFT
        if keys[pygame.K_RIGHT] and snake.direction != LEFT:
            snake.direction = RIGHT

        # Движение змейки
        if not snake.move():
            break  # Игра заканчивается при столкновении

        # Проверка на поедание еды
        if snake.body[0] == food.position:
            snake.grow(food.weight)  # Увеличение длины змейки на "вес" еды
            food.spawn()  # Генерация новой еды

        food.update()  # Обновление таймера еды
        food.draw()
        snake.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
