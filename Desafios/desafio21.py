import pygame
pygame.mixer.init()
pygame.mixer.music.load('pythonmusic.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue
pygame.quit()
