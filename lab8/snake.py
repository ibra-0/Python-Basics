import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 400, 400
CELL_SIZE = 20
FPS = 5  # Начальная скорость змейки

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Шрифт
font = pygame.font.SysFont(None, 30)

# Функция для отрисовки текста
def draw_text(text, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Функция для генерации еды в свободном месте
def generate_food(snake_body, walls):
    while True:
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        if (x, y) not in snake_body and (x, y) not in walls:
            return x, y

# Функция для создания стен
def generate_walls(level):
    walls = set()
    if level > 1:
        for i in range(0, WIDTH, CELL_SIZE):
            walls.add((i, 0))  # Верхняя стена
            walls.add((i, HEIGHT - CELL_SIZE))  # Нижняя стена
        for i in range(0, HEIGHT, CELL_SIZE):
            walls.add((0, i))  # Левая стена
            walls.add((WIDTH - CELL_SIZE, i))  # Правая стена
    return walls

# Главная функция
def main():
    running = True
    game_over = False
    
    # Начальное состояние змейки
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = (CELL_SIZE, 0)
    food = generate_food(snake, set())  # Начальная еда
    
    score = 0
    level = 1
    speed = FPS

    walls = generate_walls(level)  # Создание стен

    while running:
        screen.fill(WHITE)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)

        if not game_over:
            # Движение змейки
            new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

            # Проверка на выход за границы
            if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
                game_over = True

            # Проверка столкновения со стеной
            if new_head in walls:
                game_over = True

            # Проверка столкновения с самой собой
            if new_head in snake:
                game_over = True

            # Если игра продолжается
            if not game_over:
                snake.insert(0, new_head)

                # Проверка поедания еды
                if new_head == food:
                    score += 1
                    food = generate_food(snake, walls)

                    # Уровень повышается каждые 3 очка
                    if score % 3 == 0:
                        level += 1
                        speed += 2  # Увеличение скорости
                        walls = generate_walls(level)  # Добавление стен

                else:
                    snake.pop()  # Удаление последнего сегмента, если еда не съедена

        # Отрисовка змейки
        for segment in snake:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

        # Отрисовка еды
        pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

        # Отрисовка стен
        for wall in walls:
            pygame.draw.rect(screen, BLACK, (*wall, CELL_SIZE, CELL_SIZE))

        # Отображение счета и уровня
        draw_text(f"Score: {score}", BLACK, 10, 10)
        draw_text(f"Level: {level}", BLACK, 10, 40)

        if game_over:
            draw_text("Game Over! Press R to Restart", RED, WIDTH // 4, HEIGHT // 2)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                main()  # Перезапуск игры

        pygame.display.flip()
        clock.tick(speed)  # Установка скорости змейки

    pygame.quit()

if __name__ == "__main__":
    main()
