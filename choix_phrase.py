from .requete1 import *
import os

def lecture_liste(entree):

    c = 0
    liste = requete1()
    phrase_apres = []
    for i in liste:
        c1 = 0
        for j in liste[c]:
            #print(liste[c][c1])
            if entree == liste[c][c1]:
                phrase_apres.append(liste[c][c1 + 1])
            c1+=1
        c+=1

    return phrase_apres



def tri_liste(entrance):
    """Here we go see all matches from entrance"""

    liste = []
    for i in entrance:
        i = i.split()
        liste.extend(i)
  
    dico = {}

    c = 0
    for i in liste:
        dico[i] = -1


    for i in liste:
        for cle, valeur in dico.items():
            if i == cle:
                dico[i] += 1

    

    return dico

def analyse_dico(entree):
    print(entree)
































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





