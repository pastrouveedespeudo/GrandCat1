#on remplis la case wiki par une image gnre salut emoticone !

from conteneur import *
from conteneur_rep import *



def q_sans_rien(entree):
    conteneur()
    conteneur_reponse1()

    espace = ""


    for i in entree:
        if i == " ":
            espace = True

        else:
            espace = False

    return espace
    #si y'a un espace alors y'a un autre truk apres
    
def q_vous(entree):

    politesse = ""
    
    vous = str(entree).find("vous")
    if vous >= 0:
        politesse = True

        
    return politesse
    #si use politesse alors use polistesse


    
def rep_bonjour(entree):

    bj = ""
    
    bonjour = str(entree).find("bonjour")
    if bonjour >= 0:
        bj = True


    return bj
    #si bonjour alors on rep bonjour sinon autre hasard


def fin_debut_de_conversation():
    pass









def rep_bonjour(entree):
    pass
def rep_sans_question(entree):
    pass

def rep_avec_question(entree):
    pass


def toutes_les_3phrases():
    pass
#return blagounettte genre un truk rien a voir et on dis oups trompé

def enregistrement():
    pass
#dans un fichier comme ca on recup la convers

