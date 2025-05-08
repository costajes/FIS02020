#!/usr/bin/env python3
# -*- coding: utf-8 -*-

dir_dados = "/home/costajes/work/disciplinas/FIS02020/dados/"

#%% 1. Escrevendo em arquivo (modo texto)
file1 = dir_dados + "exemplo.txt"

with open(file1, "w") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")
    arquivo.write("Terceira linha\n")
    
#%% 2. Lendo arquivo linha por linha.

with open(file1, "r") as arquivo:
    for linha in arquivo:
        #print(linha, end='')
        print(linha.strip())
        
#%% 3. Lendo todo o conteúdo de uma vez

with open(file1, "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
print(type(conteudo))

#%% 4. Acrescentando dados no final do arquivo

with open(file1, "a") as arquivo:
    arquivo.write("Mais uma linha.\n")
    
#%% 5. Lendo e escrevendo dados tabulares
#      com CSV
import csv

file2 = dir_dados + "stars.csv"

with open(file2, "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    
    escritor.writerow(["Id", "DEC", "RA"])
    escritor.writerow(['star1', -30.001, 3.415])
    escritor.writerow(['star2', -29.232, 12.789])
    escritor.writerow(['star3', 40.123, 23.123])
    
#%% 
with open(file2, "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
        
#%% 6. Lendo dados tabulares...


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    