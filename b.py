lines = ['2', 'angleterre;suisse;italie;allemagne', 'ryan;malone;arcu;+33-8884;etas-unis', 'bruce;ellison;tortor;-33-125090826;etas-unis']

lpays = lines[1].split(';')

entreprise = []

for i in lines[2:]:
    i = i.split(";")
    entreprise.append(i)

dico = {}
yo = []
for i in entreprise:
    for j in i:
        dico[j] = 0
        
        a = dict((cle,valeur+1) for (cle, valeur) in dico.items() if cle == j)
        yo.append(a)
    
doublon = ([val for i in yo for val in i.values() if val > 1])
print(doublon)
  
a=0
b = sum([a+i for i in doublon])
print(b)































# 2 2 4
