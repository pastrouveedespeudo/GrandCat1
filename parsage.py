import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim


def no_ponctuation(entrance):
    """here we searching punctuation, and we erase it"""

    ponct = ["?", "!", ".", ","]
    new = []
    for i in entrance:
        if i == "?" or i == "!" or i == ".":
                pass
        else:
            new.append(i)


    try:
        if new[-1] == " ":
            return "".join(new[:-1])
        else:
            return "".join(new)
    except:
        pass
    return "".join(new)


def search_dico(data):
    """Here we search substantive of the next word"""

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
    """Here we deleting apostrophe and add e or a from search_dico"""

    liste = []
    liste_dico = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]
    phrase_accroche = "Salut GrandPY  Est-ce que tu connais l'adresse"

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
            c += 1
        mot = "".join(mot)
        return mot
    else:
        return data


def parsing_texte(data):
    """Here we'll go to parsing data \
    if user input sentences: Salut GrandPY ! Est-ce que tu connais l'adresse de\
    we juste take the last word from the sentece"""


    liste2 = [[], [], [], [], [], [], [], [], [], [], [], [], []]
    yoda = []
    find = 0

    phrase_accroche = "Salut GrandPY  Est-ce que tu connais la adresse"
    search = str(data).find(str(phrase_accroche))

    if search >= 0:
        for i in data:
            liste2[find].append(i)
            if i == " ":
                find += 1

        for j in liste2:
            if j == []:
                pass
            else:
                yoda.append("".join(j))
        return yoda[-1]

    else:
        return data



def searching(parametre):
    """Here we searching from Python modul(geopy.geocoders)\
    address from the input from html page"""

    geocoder = Nominatim(user_agent="run.py")
    #parametre is data recup from data()

    location = geocoder.geocode(parametre, True, 30)
    localisation = location.address
    localisation = str(localisation)

    #define data from geopy.geocoders into var
    address = location.address
    latitude = location.latitude
    longitude = location.longitude

    return address, latitude, longitude
