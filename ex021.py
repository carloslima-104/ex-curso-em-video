print("BOA MÚSICA!!!")
import pygame
pygame.init()
# Descomente a linha a seguir se desejar inicializar o módulo mixer explicitamente
# pygame.mixer.init()
pygame.mixer.music.load("../maroon.mp3")
pygame.mixer.music.play()
pygame.time.delay(50000)
pygame.mixer.music.stop()
pygame.quit()