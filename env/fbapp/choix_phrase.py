from .requete1 import *
import os

def lecture_liste(entree):

    liste = requete1()


    phrase_apres = []

    c = 0
    for i in liste:
        c1 = 0
        for j in liste[c]:
            #print(liste[c][c1])
            if entree == liste[c][c1]:
                phrase_apres.append(liste[c][c1 + 1])
            c1+=1
        c+=1


    return phrase_apres

    #PLUS OU MOINS ATTENTION







def ecriture():
    
    dernier_fichier = []

    with open("liste_phrase.py","r") as file_phrase:    #en gros la on liste les fichier de phrase
        dernier_fichier.append(file_phrase)


    new = dernier_fichier[-4:-3]
    new = str(new + 1) + ".py"

    with open(new, "a") as file:            #on ecrit le dernier titre + 1
        file.write(("    a = [['" + str(question1) + "'],"))
        



        file.write(']')

def sens_phrase():
    pass





