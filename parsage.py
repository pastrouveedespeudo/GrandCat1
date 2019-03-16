import requests

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def search_dico(data):

    path = "http://www.cnrtl.fr/definition/{}/substantif".format(data)
    
    requete = requests.get(path)
    page = requete.content
    
    soup = BeautifulSoup(page, "html.parser")      
    propriete = soup.find_all("div")

    fem = str(propriete).find("fém")
    masc = str(propriete).find("masc")

    if fem >= 0:
        
        return "nf"
    elif masc >= 0:

        return "nm"
    else:
        return "nm"


def apostrohpe(data):

   

    liste = []
    liste_dico = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    phrase_accroche = "Salut GrandPY ! Est-ce que tu connais l'adresse"
    
    a = str(data).find(str(phrase_accroche))
    
    if a >= 0:
        
        liste = []
        for i in data:        
            liste.append(i)
      

        mot = []
        c = 0
        com = 0
        for i in liste:
            if liste[c] == "'":

                for j in liste[c+1:-1]:
                    liste_dico[com].append(j)
                    if j == " ":
                        com += 1
                        break
                for i in liste_dico:
                    if i == []:
                        pass
                    else:
                        sub = search_dico("".join(i))
                        if sub == "nm":
                            liste[c] = "e"
              
                        elif sub == "nf":
                            liste[c] = "a"
                        
                            
                mot.append(liste[c])
                mot.append(" ")  
            else:
                mot.append(liste[c])    
                
            c+=1

        mot = "".join(mot)

        return mot

    else:
        return data




def parsing_texte(data):
    """Here we'll go to parsing data"""
    """if user input sentences: Salut GrandPY ! Est-ce que tu connais l'adresse de"""
    """we juste take the last word from the sentece"""




    liste = []
    liste2 = [[],[],[],[],[],[],[],[],[],[],[],[],[]]

    yoda = []
    
    c = 0
    
    phrase_accroche = "Salut GrandPY ! Est-ce que tu connais la adresse"
    a = str(data).find(str(phrase_accroche))

    if a >= 0 :

        for i in data:
            liste2[c].append(i)
            if i == " ":
                c+=1

        for j in liste2:
            if j == []:
                pass
            else:
                yoda.append("".join(j))
        print(yoda[-1])
        return yoda[-1]

    else:
        print(data)
        return data




























