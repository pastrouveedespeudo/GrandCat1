from conteneur import *
from contains import conteneur_rep 
import random
import os

def phase_une(entree):
    debut = conteneur()

    mot_commencement_politesse = ""
    #ex : ca va ?
    
    for i in debut[8]:

        if i == entree:
            mot_commencement_politesse = True
            break
            
        else:
            mot_commencement_politesse = False

    return mot_commencement_politesse


    #si mot_commencement_politesse == bonjour alors ph1



def q_vous(entree):

    politesse = ""
    
    vous = str(entree).find("vous")
    if vous >= 0:
        politesse = True
    else:
        politesse = False
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


    

    
def rep_avec_question(entree):
    pass




def fin_debut_de_conversation():
    pass







def toutes_les_3phrases():
    pass
#return blagounettte genre un truk rien a voir et on dis oups trompé

def enregistrement():
    pass
#dans un fichier comme ca on recup la convers





#-----------------------------------------

def phase_1_decide(entree, etape):



    a = phase_une(entree)

    b = q_vous(entree)

    c = amorce(entree)

    #print(a,b,c)


    rep = conteneur()

    choix = random.choice(rep[c[1]])

    etape.append(1)

    return choix




def phase_1_1_decide():
    
    if comment_ca_va == True:
        pass

    if vous == True:
        pronom = "vous"














def decide_im1(entree, etape):
    

    if etape[-1] == 1:
        print("oui")
    
        c = amorce(entree)
        
        if c[1] == 1:
            pass

        if c[1] == 1:
            pass


        if c[1] == 1:
            pass

        if c[1] == 1:
            pass
        if c[1] == 1:
            pass

        if c[1] == 1:
            pass

        if c[1] == 1:
            pass



        
        os.chdir("convers\one")
        liste = os.listdir()


    




































