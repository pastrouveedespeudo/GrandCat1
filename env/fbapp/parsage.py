"""This is methods to check the answers"""

import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim


def no_ponctuation(entrance):
    """here we searching punctuation, and we erase it"""

    new = [i for i in entrance if i != "?" and i != "!" and i != "."]

    try:
        if new[-1] == " ":
            return "".join(new[:-1])
        else:
            return "".join(new)
    except:
        pass
        #new empty user click into enter without input ?

    return "".join(new)


def search_dico(data):
    """Here we search substantive of the next word"""

    path = "http://www.cnrtl.fr/definition/{}/substantif"
    path = path.format(data)
    
    request = requests.get(path)
    page = request.content
    soup = BeautifulSoup(page, "html.parser")
    propertyy = soup.find_all("div")

    fem = str(propertyy).find("fém")
    masc = str(propertyy).find("masc")

    if fem >= 0:
        return "nf"
    elif masc >= 0:
        return "nm"
    else:
        return "nm"


def apostrohpe(data):
    """Here we deleting apostrophe and add e or a from search_dico"""

    list_dico = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]
    catchphrase = "Salut GrandPY  Est-ce que tu connais l'adresse"

    a = str(data).find(str(catchphrase))
    
    if a >= 0:
        liste = [j for i in data for j in i]

        word = []
        c = 0
        com = 0

        for i in liste:
            if liste[c] == "'":
                for j in liste[c+1:-1]:
                    list_dico[com].append(j)
                    if j == " ":
                        com += 1
                        break
          
                for i in list_dico:
                    if i == []:
                        pass
                    else:
                        try:
                            sub = search_dico("".join(i))
                            if sub == "nm":
                                liste[c] = "e"
                            elif sub == "nf":
                                liste[c] = "a"
                            else:
                                liste[c] = "e"
                        except:
                            print("!!!!!!!!!!!!!!!!\
                                    le dictionnaire en ligne n'a pas répondu\
                                    Une tentative de connexion a échoué car\
                                    le parti connecté n’a pas répondu\
                                    convenablement au-delà d’une certaine\
                                    durée ou une connexion établie a échoué\
                                    car l’hôte de connexion n’a pas répondu")
  
                word.append(liste[c])
                word.append(" ")

            else:
                word.append(liste[c])
            c += 1
        word = "".join(word)
        return word
    else:
        return data


def parsing_text(data):
    """Here we'll go to parsing data \
    if user input sentences: Salut GrandPY ! Est-ce que tu connais l'adresse de\
    we juste take the last word from the sentence"""

    catchphrase = "Salut GrandPY  Est-ce que tu connais la adresse"
    search = str(data).find(str(catchphrase))

    if search >= 0:

        separate_element = data.split()
        list_into_list = [i.split() for i in separate_element]
        join_list = [",".join(j) for i in list_into_list for j in i]
        unification = str(join_list[-1]).replace(",","")
                
 
        return unification

    else:
        return data


def searching(parameter):
    """Here we searching from Python modul(geopy.geocoders)\
    address from the input from html page"""

    geocoder = Nominatim(user_agent="run.py")
    #parametre is data recup from data()
    try:
        location = geocoder.geocode(parameter, True, 30)
        localisation = location.address
        localisation = str(localisation)

        #define data from geopy.geocoders into var
        address = location.address
        latitude = location.latitude
        longitude = location.longitude
        return address, latitude, longitude
    except:
        return "None"
