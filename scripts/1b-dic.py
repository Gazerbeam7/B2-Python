#!/usr/bin/python3
# 1b-dic.py
# saisie plusieurs prénoms, arret possible avec 'q'
# Théo Charron 
# 19/10/2018


print('entrez prenoms')

nom = input()
noms = []

while nom != 'q':
    noms.append (nom)
    nom = input()
    
print(noms)

    
    
