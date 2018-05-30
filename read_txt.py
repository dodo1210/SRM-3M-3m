# encoding=utf8
# -*- coding: utf-8 -*-
import sys
import MySQLdb

con = MySQLdb.connect(host="localhost", user="root", passwd="dodo123", db="ia")
con.select_db('ia')
cursor = con.cursor()

arq = open('musicas_tristes.txt','r')
linhas = arq.readlines()
count = 199

for l in linhas:
    nome,n = l.split("\n")
    print(nome)
    tm = 0
    tM = 0

    arqi = open('musicas_tristes/'+nome,'r')
    musica = arqi.readlines()
    for read in musica:
        m,n = read.split("\n")
        if m == "terceira maior":
            tM = tM+1
        else:
        	tm = tm +1

    cursor.execute("""
	INSERT INTO MUSICAS (COD_CLI, NOME, TERCA_MENOR, TERCA_MAIOR)
	VALUES (%s, %s, %s, %s)
	""", (count,nome,tm,tM))

    count = count+1

arq.close()

# gravando no bd
con.commit()

print('Dados inseridos com sucesso.')

con.close()