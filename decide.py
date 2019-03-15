from conteneur import *
from conteneur_rep import *
import random


def phase_une(entree):
    debut = conteneur()

    mot_commencement_politesse = ""

    
    for i in debut[3]:
        politesse = str(entree).find(i)
        if politesse >= 0:
            politessse = True
        else:
            politessse = False

    return mot_commencement_politesse


    #si mot_commencement_politesse == bonjour alors ph1



    
def q_vous(entree):

    politesse = ""
    
    vous = str(entree).find("vous")
    if vous >= 0:
        politesse = True

        
    return politesse
    #si use politesse alors use polistesse


    
def amorce(entree):

    bj = ""
    liste = 0

    
    bonjour = str(entree).find("bonjour")
    salut = str(entree).find("salut")
    coucou = str(entree).find("coucou")
    hey = str(entree).find("hey")
    heyy = str(entree).find("heyy")
    yo = str(entree).find("yo")
    hello = str(entree).find("hello")
    kikou = str(entree).find("kikou")

    if bonjour >= 0:
        bj = "bonjour"
        liste += 1
        
    elif salut >= 0:
        bj = "salut"
        liste += 2
            
    elif coucou >= 0:
        bj = "coucou"
        liste += 3
            
    elif hey >= 0:
        bj = "hey"
        liste += 4
            
            
    elif yo >= 0:
        bj = "yo"
        liste += 5
            
    elif hello >= 0:
        bj = "hello"
        liste += 6
            
    elif kikou >= 0:
        bj = "kikou"
        liste += 7
            


    return bj, liste
    #si bonjour alors on rep bonjour sinon autre hasard


    

    















def fin_debut_de_conversation():
    pass



def reponse():
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





#-----------------------------------------

def phase_1_decide(amorcage,
                   comment_ca_va,
                   vous,
                   entrance):


    try:
        amorce = conteneur()

        if vous == False:
            pronom ="tu"
            
        choix_phrase = random.choice(amorce[amorcage[1]])
        print(choix_phrase)
        
        return choix_phrase
        
    except:
        return "oups y'a eu une erruer"
##
##    if comment_ca_va == True:
##        pass
##
##    if vous == True:
##        pronom = "vous"






















