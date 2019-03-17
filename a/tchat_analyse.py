
def lower(entrance):
    low_charactere = entrance.lower()


    return str(low_charactere)

def bot(entrance):
    entrance = entrance.lower()

    no_adresse = ""
    
    print(entrance)
    conteneur_phrase = conteneur()
 
    for i in conteneur_phrase:
        for j in i:
            if j == str(entrance):
                no_adresse = True



    return no_adresse, entrance
