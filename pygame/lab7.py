import pygame
import sys
import math
import time

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mickey Clock')

WHITE = (255, 255, 255)

mickey_face = pygame.image.load('mickey_face.png')
mickey_face = pygame.transform.scale(mickey_face, (WIDTH, HEIGHT))

right_hand = pygame.image.load('right_hand.png')
left_hand = pygame.image.load('left_hand.png')

right_hand = pygame.transform.scale(right_hand, (150, 150))
left_hand = pygame.transform.scale(left_hand, (150, 150))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    screen.blit(mickey_face, (0, 0))

    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    left_angle = -seconds * 6  # 6 градусов за каждую секунду
    rotated_left_hand = pygame.transform.rotate(left_hand, left_angle)
    rect_left = rotated_left_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(rotated_left_hand, rect_left.topleft)

    right_angle = -minutes * 6  
    rotated_right_hand = pygame.transform.rotate(right_hand, right_angle)
    rect_right = rotated_right_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(rotated_right_hand, rect_right.topleft)

    pygame.display.flip()
    clock.tick(60)

