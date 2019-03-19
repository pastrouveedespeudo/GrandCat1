from .requete1 import *
from .requete2 import *
from .phrase_anecdocte import *
import os
import random


def lecture_liste(entree, liste_oui_non):
    print(liste_oui_non[-1][:-2])
    if liste_oui_non[-1] == "phrase schema":

        c = 0
        liste = requete1()
        phrase_apres = []
        for i in liste:
            c1 = 0
            for j in liste[c]:
                #print(liste[c][c1])
                if entree == liste[c][c1]:
                    try:
                        phrase_apres.append(liste[c][c1 + 1])
                    except:
                        phrase_apres.append("faut mettre d'autre phrassse")
                c1+=1
            c+=1
    elif liste_oui_non[-1][:-2] == "phrase anecdocte":
        dico_best = oui_non(entree, liste_oui_non)
        return dico_best
    
    try:
    
        dico_best = tri_liste(phrase_apres)
        liste_oui_non.append("phrase schema")
        
    except:
        
        liste_oui_non.append("phrase anecdocte")
        dico_best = dico_best_empty(entree, liste_oui_non)
   
     

        
    return dico_best



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

    dico_best = max(dico)

    return dico_best








