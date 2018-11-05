#!/usr/bin/python3
# 1a-add.py
# demander 2 nombres, afficher résultat addition des deux
# Théo Charron
#


inta = input()
intb = input()

if inta.isdigit():
    inta = int(inta)
else:
    print('Entrez un nombre')
    inta = int(input())

if intb.isdigit():
    intb = int(intb)
else: 
    print('Entrez un nombre')
    intb = int(input())

print(inta + intb)
	

	


