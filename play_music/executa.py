#!/usr/bin/env python
import pygame
from Tkinter import *
file = '/home/douglas/Documentos/Trabalho_IA/play_music/chaves-musica-triste.mp3'
root = Tk()
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
root.mainloop()