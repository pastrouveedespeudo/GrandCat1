"""Here we decide of the sentence to put according to the answer"""

from .ecriture import *
from .requete1 import *
from .requete2 import *
from .phrase_anecdocte import *


def lecture_liste(entree, liste_oui_non):
    """here we choose to put a logical continuation\
    sentence of an existing conversation or we put\
    an anecdotal sentence so that we can refocus\
    the discussion and be able to collect\
    the non-existing sentence"""

    if liste_oui_non[-1] == "phrase schema":
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
                        pass
                compteur1 += 1
            compteur += 1

    elif liste_oui_non[-1][:-2] == "phrase anecdocte":
        dico_best = oui_non(entree, liste_oui_non)
        return dico_best
    try:
        dico_best = tri_liste(phrase_apres)
        liste_oui_non.append("phrase schema")
    except:
        #ecriture(entree)
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
    compteur = 0
    for i in liste:
        dico[i] = -1

    for i in liste:
        for cle, valeur in dico.items():
            if i == cle:
                dico[i] += 1

    dico_best = max(dico)

    return dico_best
