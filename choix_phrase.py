"""here we decide which sentence we will put"""

from .requete1 import *
from .requete2 import *
from .phrase_anecdocte import *


def lecture_liste(entree, liste_oui_non):
    """Here we matching sentences with requete1"""

    compteur = 0
    liste = requete1()
    phrase_apres = []
    for i in liste:
        compteur1 = 0
        for j in liste[compteur]:
            if entree == liste[compteur][compteur1]:
                try:
                    phrase_apres.append(liste[compteur][compteur1 + 1])
                except:
                    phrase_apres.append("faut mettre d'autre phrassse")
            compteur1 += 1
        compteur += 1

    try:
        dico_best = tri_liste(phrase_apres)
        liste_oui_non.append("phrase schema")
    except:
        dico_best = "faut mettre d'autre phrassse"
        liste_oui_non.append("phrase anecdocte")

    return dico_best


def tri_liste(entrance):
    """Here we go see all matches from entrance"""

    liste = []
    for i in entrance:
        liste.append(i)
    for i in liste:
        i = i.split()

    dico = {}

    for i in liste:

        dico[i] = -1


    for i in liste:
        for cle, valeur in dico.items():
            if i == cle:
                dico[i] += 1

    dico_best = max(dico)

    return dico_best
