#--------------------------------------------------------------------------------------
#                                    Imports
#--------------------------------------------------------------------------------------

import csv
from genericpath import exists
import tkinter as tk
import re
from PIL import Image, ImageTk
from tkinter import X, font as tkfont

#--------------------------------------------------------------------------------------
#                                    Classes
#--------------------------------------------------------------------------------------

class Description:
    
    #Constructeur
    def __init__(self, mot:str, coord):
        self.mot = mot
        self.coord = coord


class Film:
    
    #Constructeur
    def __init__(self,titre:str,realisateur:str, genre:str,descri:Description):
        self.titre = titre
        self.realisateur=realisateur
        self.genre = genre
        self.description = descri

    def toString(self):
        #retourne une chaine de caractère décrivant l'instance
        string = ("titre:"+self.titre +";réalisateur:"+self.realisateur+";genre:"
        +self.genre+";plot_keywords:"+str(self.description)) 
        return string



class Mot:

    #Constructeur
    def __init__(self, mot:str):
        self.mot = mot 
        self.nb_occurence=1

    def add(self):
        #ajoute 1 au nombre d'occurence
        self.nb_occurence +=1
    
    def toString(self):
        #retourne une chaine de caractère décrivant l'instance
        string = ("Mot : "+self.mot +" ; Nombre d'occurence : "+str(self.nb_occurence)) 
        return string

#--------------------------------------------------------------------------------------
#                            Fonctions et Procédures
#--------------------------------------------------------------------------------------

#-------------------------------------Tests--------------------------------------------

def test1():
    print("Valider")
    
def test2():
    print("Annuler")

def clean_plot_keywords(string: str, 
    punctuations=r''' !()-[]{};:'"\,<>./?@#$%^&*_~''') -> list[str]:
     # On supprime la ponctuation
    for x in string: 
        #pour tout les mots contenus dans string
        #string est sous la forme (mot1|mot2 etc)
        if x in punctuations: 
            #si la chaine de caratère contient un signe de ponctuation du tableau 
            #ponctuation
            string = string.replace(x, "|") 
            #on remplace la ponctuation par |
    string = string.lower() #on met les chaines de caractères sous forme de miniscule
    string = re.sub(r'\s+', ' ', string).strip()
    tab=string.split('|')
    return tab

def lecture():
    #fonction qui permet de lire le fichier .cvs et renvoie ce qu'il contient
    with open("movie_metadata.csv",encoding="utf8", mode="r") as cvs_file:
        #on ouvre le fichier csv
        csv_reader=csv.DictReader(cvs_file, delimiter=";")
        line_count = 0
        liste = []
        for row in csv_reader:
            #on parcourt toutes les lignes du fichier
            #-----------il faut traiter ces données (voir sujet)---------------
            movie_title=row['movie_title']
            director_name=row['director_name']
            genres=row['genres']
            plot_keywords=row['plot_keywords']
            tab_plot_keywords = clean_plot_keywords(plot_keywords)
            #------------------------------------------------------------------
            film = Film(movie_title,director_name,genres,tab_plot_keywords)
            liste.append(film)
            line_count += 1
        print(f'On a parcourut {line_count} lignes.')
        
        all_words= []
        for i in liste:
            for x in i.description:
                all_words.append(x)

        list_words(all_words)


def list_words(all_words : list[str]):
    #fonction qui retourne la liste de tous les plots_keywords, sans répétition
    #(chaque mot sera contenu une seule et unique fois dans la liste)
    
    liste =[] #initialisation d'une liste qu'on va remplir au fur et à mesure
    for word in all_words:
        #pour tout les mots de la liste de mots
        test=False #initialisation d'une variable de test qui se réinitialise à 
                   #chaque itération de la boucle
        for x in liste:
            #pour tout les mots de la liste
            if x.mot==word:
                #si le mot de la liste est identique à celui de all_words
                #alors le mot contenu de la liste all_words est deja contenu dans liste
                x=x.add() #on ajoute 1 au nombre d'itération
                test=True   
    
        if test==False:
            #si word n'a pas été trouvé dans liste
            print(word + " n'est pas dans la liste (fin)")
            #alors on l'ajoute
            liste.append(Mot(word))
                  
    return liste
        

#-------------------------------------Main---------------------------------------------

lecture()