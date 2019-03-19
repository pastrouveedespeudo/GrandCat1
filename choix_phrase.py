from .requete1 import *
from .requete2 import *
import os
import random



def lecture_liste(entree, liste_oui_non):

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
   
    #liste_oui_non.append("reponse schéma")

    try:
        dico_best_phrase = tri_liste(phrase_apres)
        best_phrase = analyse_dico(dico_best_phrase, liste_oui_non)
    except:
        best_phrase = "PLUS DE PHRASEE"
    
    return best_phrase


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

def analyse_dico(entree, liste_oui_non):

    try:
        dico_best = max(entree)
        liste_oui_non.append("réponse schéma")
        return dico_best
    except:
        dico_best = dico_best_empty(entree, liste_oui_non)
        return dico_best





def dico_best_empty(entree, liste_oui_non):

    #choix_aleatoire = random.choice(3)
    
    #1 une anecdote
    choix_aleatoire = 1
    if choix_aleatoire == 1:
        
        reponse = requete2()
        
        longueur_conteneur2 = len(reponse) - 1
        hasard = random.randint(0, longueur_conteneur2)

        liste_oui_non.append("phrase anecdocte "+str(hasard))

        print(reponse[hasard][0],"POZINI BUTTTTTTTT")




        return reponse[hasard]


def oui_non(oui_non, entree):
    cont = requete2()
    

    liste_oui = ["oui"]
    liste_non = ['non']

    conteneur_rep = cont[int(entree[-1])]
    
    for i in liste_oui:
        if oui_non == i:
            return conteneur_rep[1], "fin anecdocte"

        
    for i in liste_non:
        if oui_non == i:
            return conteneur_rep[2], "fin anecdocte"




    #2 une question

    #3 on reprend la reponse et on fait comme eliza

    #sortie = str(entree)
    
    #return sortie
    #on doit ajouter la reponse dans notre truk


    #4 oui dis moi et on marque la prochaine phrase
    #on doit ajouter " "















