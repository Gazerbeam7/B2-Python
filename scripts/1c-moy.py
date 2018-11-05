#!/usr/bin/python3
# 1c-moy.py
# saisie 1 prénom, 1 note pour plusieurs personnes, 'q' pour stop, moyenne, top 5
# Théo Charron
# 16/10/2018


import re

bulletin = []
strNom = 'Nom'
strGrade = 'grade'
cpt = 0
tot = 0

userInput = input('Student\'s name and grade: ')

# on verifie si la valeur peut être passé en float et si c'est en dessous de 20
# on retourne un bouleéen
def is_number(s):
    try:
        float(s)
        if float(s)<=20.0:
            return True
        else:
            return False
    except ValueError:
        return False

# on regarde si le string passé est conforme avec un booléen
def is_good(str):
    if re.match(r"[a-zA-Z][^#&<>\"~;$^%{}?]", str) is not None:
        return True
    else:
        return False

