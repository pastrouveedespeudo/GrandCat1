"""here we are going to write the sentences that requete1 does not have
and we write in"""

def ecriture(entree):
    """we opening requete1 source of our sentences"""
    liste = []

    fichier = open("fbapp/requete1.py", "r")

    liste.append(fichier.read())

    liste[0] = liste[0][:-17]
    print(liste[0][-2:])
    print("ty")
    with open("fbapp/requete1.py", "w") as file:
        file.write((str(liste[0][:-2])\
                    + "\n"\
                    + "           [" + '"' +str(entree) + '"]'\
                    +"," + "\n"\
                    + "           ]" + '\n'\
                    +"    "+"return liste"))
