import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
start_pos = None
shape = "square"  

def draw_square(surface, start, end):
    size = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
    pygame.draw.rect(surface, RED, (*start, size, size), 2)

def draw_right_triangle(surface, start, end):
    pygame.draw.polygon(surface, GREEN, [start, (start[0], end[1]), (end[0], end[1])], 2)

def draw_equilateral_triangle(surface, start, end):
    side = abs(end[0] - start[0])
    height = (math.sqrt(3) / 2) * side
    pygame.draw.polygon(surface, BLUE, [start, (start[0] + side, start[1]), (start[0] + side // 2, start[1] - height)], 2)

def draw_rhombus(surface, start, end):
    width = abs(end[0] - start[0])
    height = abs(end[1] - start[1])
    center = (start[0] + width // 2, start[1] + height // 2)
    pygame.draw.polygon(surface, BLACK, [(center[0], start[1]), (end[0], center[1]), (center[0], end[1]), (start[0], center[1])], 2)

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            if shape == "square":
                draw_square(screen, start_pos, end_pos)
            elif shape == "right_triangle":
                draw_right_triangle(screen, start_pos, end_pos)
            elif shape == "equilateral_triangle":
                draw_equilateral_triangle(screen, start_pos, end_pos)
            elif shape == "rhombus":
                draw_rhombus(screen, start_pos, end_pos)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
