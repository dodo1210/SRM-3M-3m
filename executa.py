# -*- coding: utf-8 -*-
#!/usr/bin/env python
#import thread # should use the threading module instead!
from threading import Thread
import base64
import subprocess
from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
import PIL.ImageTk
import pygame

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "20")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 10
        self.segundoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="SRM")
        self.titulo["font"] = self.fontePadrao
        self.titulo.pack()

        self.busca = Entry(self.primeiroContainer)
        self.busca["font"] = ("Arial", "12")
        self.busca["width"] = 30
        self.busca.pack(side=LEFT)

        im = PIL.Image.open("imagem/lupa.png")
        photo = PIL.ImageTk.PhotoImage(im)

        self.botao = Button(self.primeiroContainer, image=photo)
        self.botao.im = photo  # keep a reference!
        self.botao["command"] = self.pesquisa
        self.botao.pack()

        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox = Listbox(master, yscrollcommand=scrollbar.set)
        for i in range(20):
            listbox.insert(END, str(i))
        listbox.pack(fill=BOTH, expand=1)

        scrollbar.config(command=listbox.yview)

        im_play = PIL.Image.open("imagem/play.png")
        photo_play = PIL.ImageTk.PhotoImage(im_play)

        self.play = Button(self.segundoContainer, image=photo_play)
        self.play.im_play = photo_play  # keep a reference!
        self.play["command"] = self.play_music
        self.play.pack(side=LEFT)

        self.musica = Label(self.segundoContainer, text="Você esta ouvindo")
        self.musica["font"] = ("Arial", "12")
        self.musica.pack()

    def play_music(self):
        file = '/home/douglas/Documentos/Trabalho_IA/play_music/chaves-musica-triste.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        inicio.mainloop()

    def pesquisa(self):
        busca = Tk()
        Busca(busca)
        busca.mainloop()
   		
class Busca:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "20")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 10
        self.segundoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Você pesquisou por: The lazy song")
        self.titulo["font"] = self.fontePadrao
        self.titulo.pack()

        self.autenticar = Button(self.segundoContainer)
        self.autenticar["text"] = "The lazy song"
        self.autenticar["font"] = self.fontePadrao
        self.autenticar["width"] = 12
        self.autenticar.pack()

    def play_music(self):
        file = '/home/douglas/Documentos/Trabalho_IA/play_music/chaves-musica-triste.mp3'
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        inicio.mainloop()

    def pesquisa(self):
        print("oio")
      	

        

inicio = Tk()
inicio.config(height=500, width=500)

Application(inicio)
inicio.mainloop()