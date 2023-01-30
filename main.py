from random import randint
import time

def tableau(x):

    tab = [[0] * (x + 2)]+[[0]+[randint(0,1) for largeur in range(x)]+[0] for hauteur in range(x - 2)] + [[0] * (x + 2)]
    return tab

def affiche1(tab):
    for indice in range(len(tab)):
        print(tab[indice])

def affiche2(tab):
    for i in range(1,len(tab)):
        for j in range(1,len(tab[i])-1):
            if tab[i][j] == 0: 
                c = " - "
            elif tab[i][j] == 1:
                c = " X "
            print(c, end="")
        print("\n")

def verifCases(tab, hauteur, largeur):
    total = 0
    cellule = tab[largeur][hauteur]
    if tab[largeur-1][hauteur-1] == 1:
        total += 1
    if tab[largeur][hauteur-1] == 1:
        total += 1
    if tab[largeur+1][hauteur-1] == 1:
        total += 1

    if tab[largeur-1][hauteur] == 1:
        total += 1
    if tab[largeur+1][hauteur] == 1:
        total += 1
    
    if tab[largeur-1][hauteur+1] == 1:
        total += 1
    if tab[largeur][hauteur+1] == 1:
        total += 1
    if tab[largeur+1][hauteur+1] == 1:
        total += 1

    if total == 3:
        cellule = 1
    elif total <2 or total >3:
        cellule = 0
    return cellule

def etapeSuivante(tab, x):
    nvTableau = [[0] * (x + 2)]+[[0]+[randint(0,1) for largeur in range(x)]+[0] for hauteur in range(x - 2)] + [[0] * (x + 2)]
    for largeur in range (1,len(tab)-1):
        for hauteur in range(1,len(tab[largeur])-1):
            nvTableau[largeur][hauteur] = verifCases(tab, hauteur, largeur)
    return nvTableau



def start(x):
    a = tableau(x)
    affiche2(a)
    verif = [[0] * (x + 2)]+[[0]+[randint(0,0) for largeur in range(x)]+[0] for hauteur in range(x - 2)] + [[0] * (x + 2)]
    while a != verif:
        print("\n")
        a = etapeSuivante(a, x)
        affiche2(a)
        time.sleep(0.8)

start(10)