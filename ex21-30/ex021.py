# Tocando um áudio usando o pygame
import pygame
pygame.init()
pygame.mixer.music.load('ex21-30/ex021crash.mp3')
pygame.mixer.music.play()
pygame.event.wait()
