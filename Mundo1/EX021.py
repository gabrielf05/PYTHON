#salvar como ex21.mp3
# ex21.mp3 precisa ser um arquivo de áudio e importar para dentro do VSCODE
# pip install pygame

import pygame 
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()