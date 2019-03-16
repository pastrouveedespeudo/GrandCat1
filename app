import os
import subprocess  
from geopy.geocoders import Nominatim
import request
from bs4 import *
import urllib.request
from PIL import Image
from flask import Flask
from flask import request
from flask import url_for
from flask import jsonify
from geopy.geocoders import Nominatim
from flask import render_template
from datetime import datetime
import requests
import wikipediaapi
import random
import time
from conteneur import *
from decide import *
from parsage import *


app = Flask(__name__)



LISTE = []
LISTE_PHRASE = []
LISTE_WIKI = []
LOCALISATION_WIKI = []

LISTE_PAYS = [" France", " France métropolitaine", " Paris"]


                 
@app.route('/')
def home():
    """Here we just display home page"""

    title_page = "HOME"
    return render_template("home.html",title_page=title_page)









@app.route('/wiki', methods=["GET", "POST"]) 
def wiki():
    b = ""
    liste = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    c = 0
    
    data_wiki = request.form['data']
    if data_wiki == "":
        page = ""
        return jsonify({'data':page})
    else:
        nettoyage = apostrohpe(data_wiki)
        dernier_mot = parsing_texte(nettoyage)
        search = searching(dernier_mot)

        adresse = []
        adresse.append(search[0])
        for i in adresse:
            for j in i:
                liste[c].append(j)
                if j == ',':
                    c+=1



    sentence_from_grandpy = ["Savez tu que :", "T'avais-je dis que :",
                             "Une fois on m'a dit que :"]
    
    choix = random.choice(sentence_from_grandpy)

    
    element = "".join(liste[2][:-1])
    print(element)
    wiki_wiki = wikipediaapi.Wikipedia('fr')
    page_py = wiki_wiki.page('{}'.format(element))
    existe = page_py.exists()
    if existe == True:
        page = ("<p style='color:black; font-size:1.5em;'><strong>" + str(choix)\
                +"</strong>" + "<br>"\
                + str(page_py.sections[0:200]) + "...</p>")
        
        return jsonify({'data':page})

    else:
        page = "<p style='color:black; font-size:1.5em;'>Oups je n'ai rien trouvé</p>"
        return jsonify({'data':page})
        





@app.route('/data', methods=["GET", "POST"])
def data():
    """Here, we just recup data with request form"""
    """from jquerry function() who define content from input"""

    data = request.form['data']

    nettoyage = apostrohpe(data)

    
    dernier_mot = parsing_texte(nettoyage)

    date = datetime.now()
    date = str(date)
    
    LISTE.append("<div style='font-style:italic;font-size:1.3em; color:black;'>A {}</div>".format(date))

    LISTE.append("<div style='color:black; font-size:1.3em;'><strong>Votre question: </strong></div>")
    LISTE.append("<div style='font-style:italic;font-size:1.3em; color:black;'>{}</div>".format(data))
    

    
    if data:
        
        var = searching(dernier_mot)
       
        LISTE.append("<div style='font-style:italic;font-size:1.5em;color:black;'><strong>Chat alors une addresse trouvée: </strong></div>")
        LISTE.append("<div style='font-size:1.5em; color:black;'><strong>{}</strong></div>".format(var[0]))
        LISTE.append("<br>")
        
        return jsonify({'data':LISTE})



    return jsonify({'error':'...'})













    
@app.errorhandler(404)
def page_not_found(error):
    
    return render_template("errors/404.html"), 404


if __name__== "__main__":
    

    app.run(debug=True)
   