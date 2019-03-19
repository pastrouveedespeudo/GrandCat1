from .requete1 import *
import os

def ecriture(entree):


    liste = []

    fichier = open("fbapp/requete1.py","r")

    liste.append(fichier.read())

    print(liste[0])
    print("-----------------")
    print(liste[0][-19:])
    liste[0] = liste[0][:-17]
    print(liste)


    
    with open("fbapp/requete1.py", "w") as file:
        file.write((str(liste[0][:-17])\
                    + "\n"\
                    + "           [" + '"' +str(entree) + '"]'\
                    +"," + "\n"\
                    + "           ]" + '\n'\
                    +"    "+"return liste"))









