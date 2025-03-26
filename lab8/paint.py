import pygame

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 500, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
screen.fill(WHITE)

# Инструменты
DRAW_FREE = "free"
DRAW_RECT = "rect"
DRAW_CIRCLE = "circle"
ERASER = "eraser"

# Начальные значения
drawing = False
start_pos = (0, 0)
color = BLACK
tool = DRAW_FREE
radius = 10  # Размер кисти / ластика

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tool = DRAW_FREE
            elif event.key == pygame.K_2:
                tool = DRAW_RECT
            elif event.key == pygame.K_3:
                tool = DRAW_CIRCLE
            elif event.key == pygame.K_4:
                tool = ERASER
            elif event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            if tool == DRAW_RECT:
                pygame.draw.rect(screen, color, (*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 2)
            elif tool == DRAW_CIRCLE:
                radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5 / 2)
                pygame.draw.circle(screen, color, start_pos, radius, 2)

        elif event.type == pygame.MOUSEMOTION and drawing:
            if tool == DRAW_FREE:
                pygame.draw.line(screen, color, start_pos, event.pos, 2)
                start_pos = event.pos
            elif tool == ERASER:
                pygame.draw.circle(screen, WHITE, event.pos, radius)

    pygame.display.flip()

pygame.quit()
