from random import randint

def tableau(x):

    tab = [[0] * (x + 2)]+[[0]+[randint(0,1) for largeur in range(x)]+[0] for hauteur in range(x - 2)] + [[0] * (x + 2)]
    return tab

#def affiche1(tab):
#    for indice in range(len(tab)):
#        print(tab[indice])

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
    pass

a = tableau(6)
affiche2(a)
#verifCases(a, )