from conteneur import *
from conteneur2 import *

from contains import conteneur_rep 
import random
import os

def phase_une(entree):
    debut = conteneur()

    mot_commencement_politesse = ""
    #ex : ca va ?
    
    for i in debut[8]:
        
        pol = str(entree).find(str(i))
        
        if pol >= 0:
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


    
def mot_entree(nombre):
    dico = {
        1:"bonjour", 2:"salut",3:"coucou", 4:"hey", 5:"yo", 6:"hello", 7:"kikou"
        }

    a = random.choice
    return dico[nombre]



def phase_1_decide(entree, etape):



    a = phase_une(entree)

    b = q_vous(entree)

    c = amorce(entree)

    #print(a,b,c)

    if a == False:
        #juste bonjour
        rep = conteneur()

        choix = random.choice(rep[c[1]])

        etape.append(1)

        return choix


    elif a == True and b == False:
        #bonjour ca va ?

        rep = conteneur2()

        c = amorce(entree)
        mot_amorce = mot_entree(c[1])
        #print(mot_amorce)
        

        rep_tchat = random.choice(rep)
        #print(rep_tchat)


        la_rep = mot_amorce + " " + rep_tchat
        
        return la_rep


    
    elif b == True:
        pass





def etape2(entree):

    entrance = conteneur2()

    ok = ""

    for i in entrance[1]:
        cherche = str(entree).find(str(i))
        print(cherche)
        if cherche >= 0:
            ok = True

    if ok == True:
        reponse = random.choice(entrance[2])
        print(reponse)
        return reponse, True

    else:
        return "", False

    return reponse, True


    #ok ta pensée : plusieurs issues, mais que quelques une sont correctes;
            #aller dans le meme sens ou pas
            #soit la personne cherche un comme elle soit un différent
            #selon ce quelle a deja.
            #prend le groupe de 2 personnes different la brune et la blonde le timide et lextra
            #prend le  groupe des 3 personnes lintello le bo et le sociable
            #au delas c un group de pote pas damis
            #chaque groupe damis va chercher dautre groupe soit en paix soit en conflit
            #conflit afiin de changer ca va casser le groupe
            #ou le renforcer

            #approche de groupe == ca va casser le groupe forcement
            #donc tu pourras jamais faire ca et ca depend des personnalités aussi
            
            #donc la tu dois guidée l'echange mais je sais pas comment, normalement c avec des questions
            #en "soumettant" ou en montrant on est pareil
            #donc la faut pas soumettre ni sucer il faut poser des questions en donnant donc
            #faut prendre et donner sans que ce soit visible
        #utilise les mots généralisés

        #ok imite juste eliza^^

    def essais2():
        pass
    #si on me pose une question je dois reprendre les mots et ajouter une petite touche


    def essais1():
        pass
    #mais avant on doit faire parler et pour faire parler c avec des questions ouverte


    def essais():
        pass
    #on prend la meilleur phrase





























def phase_1_1_decide():
    
    if comment_ca_va == True:
        pass

    if vous == True:
        pronom = "vous"















def picture(entrance, number, path):


    if entrance == number:
        
        os.chdir(path)
        liste = os.listdir()
        image = random.choice(liste)

        return str(image)
            

def decide_im1(entree, etape):


    if etape[-1] == 1:

        c = amorce(entree)

        bnj = picture(c[1], 1, r"C:\Users\jeanbaptiste\env\fbapp\convers\one\bonjour")
        
        slt = picture(c[1], 2, r"C:\Users\jeanbaptiste\env\fbapp\convers\one\salut")
        
        cc = picture(c[1], 3, r"C:\Users\jeanbaptiste\env\fbapp\convers\one\coucou")

        hey = picture(c[1], 4, r"C:\Users\jeanbaptiste\env\fbapp\convers\one\hey")

        yo = picture(c[1], 5, r"C:\Users\jeanbaptiste\env\fbapp\convers\one\bonjour")
            
        hello = picture(c[1], 6, r"C:\Users\jeanbaptiste\env\fbapp\convers\one\hello")
            
        kikou = picture(c[1], 7, r"C:\Users\jeanbaptiste\env\fbapp\convers\one\salut")

    return bnj, slt, cc, hey, yo, hello, kikou

        
        



    




































