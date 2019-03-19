from .requete1 import *
from .requete2 import *
import random


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

        return reponse[hasard][0]

    
def oui_non(oui_non, entree):
    cont = requete2()
    

    liste_oui = ["oui"]
    liste_non = ['non']

    conteneur_rep = cont[int(entree[-1][-1])]
    print(conteneur_rep,"clinstiwoooooooooooooooooood")
    for i in liste_oui:
        if oui_non == i:
            return conteneur_rep[1], "fin anecdocte"

        
    for i in liste_non:
        if oui_non == i:
            return conteneur_rep[2], "fin anecdocte"








        
