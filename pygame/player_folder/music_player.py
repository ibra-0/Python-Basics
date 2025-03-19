import pygame
import sys
import os

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)  # Максимальная громкость

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Music Player')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Список файлов
music_files = ['song1.mp3', 'song2.mp3', 'song3.mp3']
current_track_index = 0
playing = False

def play_music():
    global playing
    pygame.mixer.music.load(music_files[current_track_index])
    pygame.mixer.music.play()
    playing = True

def stop_music():
    global playing
    pygame.mixer.music.stop()
    playing = False

def next_music():
    global current_track_index
    stop_music()
    current_track_index = (current_track_index + 1) % len(music_files)
    play_music()

def previous_music():
    global current_track_index
    stop_music()
    current_track_index = (current_track_index - 1) % len(music_files)
    play_music()

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play / Pause
                if playing:
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_s:  # Stop
                stop_music()
            elif event.key == pygame.K_n:  # Next
                next_music()
            elif event.key == pygame.K_b:  # Previous
                previous_music()

    font = pygame.font.SysFont(None, 30)
    text = font.render(f'Now Playing: {music_files[current_track_index]}', True, BLACK)
    screen.blit(text, (20, 140))
    
    pygame.display.flip()
    clock.tick(60)
