import pygame
import sys

# Инициализация Pygame
pygame.init()

WIDTH, HEIGHT = 300, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Red Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed = 20

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP] and ball_y - ball_radius - ball_speed >= 0:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y + ball_radius + ball_speed <= HEIGHT:
        ball_y += ball_speed
    if keys[pygame.K_LEFT] and ball_x - ball_radius - ball_speed >= 0:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x + ball_radius + ball_speed <= WIDTH:
        ball_x += ball_speed
    
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    
    pygame.display.flip()
    clock.tick(60)
