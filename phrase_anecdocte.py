"""here we select a random sentence so we can write
    a new sentence in our file and redirect the conversation"""

import random
from .requete1 import *
from .requete2 import *


def dico_best_empty(entree, liste_oui_non):
    """we select random sentence"""

    #choix_aleatoire = random.choice(3)
    #1 une anecdote
    choix_aleatoire = 1
    if choix_aleatoire == 1:
        reponse = requete2()
        longueur_conteneur2 = len(reponse) - 1
        hasard = random.randint(0, longueur_conteneur2)
        liste_oui_non.append("phrase anecdocte "+str(hasard))
        return reponse[hasard][0]


def oui_non(oui_non, entree):
    """if the list contains anecdote sentence
    and that answer and yes we return a sentence"""

    cont = requete2()

    liste_oui = ["oui"]
    liste_non = ['non']

    conteneur_rep = cont[int(entree[-1][-1])]
    print(conteneur_rep, "clinstiwoooooooooooooooooood")
    for i in liste_oui:
        if oui_non == i:
            entree.append("fin anecdocte")
            return conteneur_rep[2]

    for i in liste_non:
        if oui_non == i:
            entree.append("fin anecdocte")
            return conteneur_rep[1]
