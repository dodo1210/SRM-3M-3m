#!/usr/bin/env
# -*- coding: utf-8 -*-
from pydub import AudioSegment

arq = open('/home/douglas/Documentos/Trabalho_IA/musicas_tristes.txt','r')
linhas = arq.readlines()

for l in linhas:
	m,n = l.split("\n")
	print(m)
	sound = AudioSegment.from_mp3('/home/douglas/Documentos/Trabalho_IA/musicas_tristes/'+m)
	sound.export('/home/douglas/Documentos/Trabalho_IA/musicas_tristes/'+m+".wav", format="wav")
