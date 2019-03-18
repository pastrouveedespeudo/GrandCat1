from .requete1 import *
from .requete2 import *
import os
import random

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
        liste.append(i)
    for i in liste:
        i = i.split()
        
  
    dico = {}

    c = 0
    for i in liste:
        
        dico[i] = -1


    for i in liste:
        for cle, valeur in dico.items():
            if i == cle:
                dico[i] += 1
    return dico



def analyse_dico(entree, premiere_entree):

    try:
        dico_best = max(entree)
        return dico_best, " "
    except:
        dico_best = dico_best_empty(premiere_entree)
        return dico_best



        
    



def dico_best_empty(entree):
    print(entree)

    #1 une anecdote
    #random.choice(3)

    a = cont2()
    return a


    #2 une question

    #3 on reprend la reponse et on fait comme eliza

    #sortie = str(entree)
    
    #return sortie
    #on doit ajouter la reponse dans notre truk


    #4 oui dis moi et on marque la prochaine phrase
    #on doit ajouter " "

def cont2():
    reponse = requete2()

    longueur_conteneur2 = len(reponse) -1
    hasard = random.randint(0, longueur_conteneur2)

    reponse[hasard]
    
    return reponse[hasard][0], "cont2"


def oui_non(oui_non, entree):
    pass
    #on recup "cont2" on recup lentree et si le type a dit oui ou non


#soit faire un systeme de liste avec le conteneur appropriere
#on reserve les oui, oui je saivais ouais et non je savais pas
#et on met if question1 == oui ect
#on reprend le dernier conteneur et on on met +1 pour non + 2 pour oui

#ohhhhhhh bonneuh mere y'a american gods















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





