import requests
from bs4 import BeautifulSoup

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
    print(a)
    if a >= 0:
        
        yo = data.split()
        print(yo)
        yii = [yo.index(i) for i in yo for j in i if j == "'"]
        print(yii)
        ya = [i for i in yo for j in i if j == "'"]
        print(ya)
        yu = [i.replace("'", " ") for i in ya]
        print(yu)
        ye = [i.split() for i in yu]
        print(ye)
        yi = [i[1] for i in ye]
        print(yi)
        yy = [search_dico(i) for i in yi]
        print(yy)
        yj = list(set([yo[i] for j in yo for i in yii]))
        print(yj)
        yyy = [(i,j) for i in yii for j in yy]
        yyy = list(set(yyy))
        print(yyy)

        
a = apostrohpe("Salut GrandPY  Est-ce que tu connais l'adresse l'ardoise")
print(a)




























































