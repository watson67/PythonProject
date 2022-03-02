#--------------------------------------------------------------------------------------
#                                    Imports
#--------------------------------------------------------------------------------------

import csv
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font as tkfont

def test1():
    print("Valider")
    
def test2():
    print("Annuler")
    
#--------------------------------------------------------------------------------------
#                                  Interface
#--------------------------------------------------------------------------------------


#-------------------------------Page d'accueil-----------------------------------------

def clear_frame(base_frame):
   for widgets in base_frame.winfo_children():
      widgets.destroy()

def page1(root, base_frame, theme):
    
    global img
    clear_frame(base_frame)
    #creer des frames
    PageAccueil= tk.Frame(base_frame, bg=theme[0], bd=1)
    frame1 = tk.Frame(PageAccueil, bg=theme[0], bd=1, relief=tk.SUNKEN) 
    frame2 = tk.Frame(PageAccueil, bg=theme[0], bd=1) 
    frame3 = tk.Frame(PageAccueil, bg=theme[0], bd=1) 

    c = tk.Canvas(PageAccueil, bg=theme[0], bd=0, width=300, height=100, highlightthickness=0)
    c.pack()
    #Textes 
    titre = tk.Label(frame1, text="Bienvenue sur blabla", font =("Ralewayl",40), bg=theme[0], fg=theme[1])
    titre.pack()

    soustitre = tk.Label(frame1, text="Développée par Waechter Thibaut", font =("Raleway",30), bg=theme[0], fg=theme[1])
    soustitre.pack()

    #Boutons
    #Bouton valider
    browse_txt = tk.StringVar()
    browse_btn = tk.Button(frame2, textvariable=browse_txt, padx = 50 , pady = 20, command=lambda:recommandation(root, base_frame, theme), font="Raleway", bg=theme[0], fg=theme[1])
    browse_txt.set("Recommandations")
    browse_btn.pack(side= tk.LEFT)

    #Bouton annuler
    txt = tk.StringVar()
    browse_btn = tk.Button(frame2, textvariable=txt,padx = 49 , pady = 20, command=lambda:word_embedding(root, base_frame, theme), font="Raleway", bg=theme[0], fg=theme[1])
    txt.set("Word embedding")
    browse_btn.pack()

    #Bouton Paramètres
    txt = tk.StringVar()
    browse_btn = tk.Button(frame3, textvariable=txt,padx =60 , pady = 20, command=lambda:settings(root, base_frame, theme), font="Raleway", bg=theme[0], fg=theme[1])
    txt.set("Settings")
    browse_btn.pack(side= tk.LEFT)

    #Bouton Quitter
    txt = tk.StringVar()
    browse_btn = tk.Button(frame3, textvariable=txt,padx = 70 , pady = 20, command=root.destroy, font="Raleway", bg=theme[0], fg=theme[1])
    txt.set("Exit app")
    browse_btn.pack()
    vide = tk.Canvas(PageAccueil, bg = theme[0], bd=0, width=100, height=100, highlightthickness=0)


    #ajouter
    frame1.pack(expand=tk.YES)
    vide.pack(expand=tk.YES)
    frame2.pack(expand=tk.YES)
    frame3.pack(expand=tk.YES)


    # création d'un canvas
    canvas = tk.Canvas(PageAccueil, bg=theme[0], bd=0, width=300, height=200, highlightthickness=0)

    # logo
    img = ImageTk.PhotoImage(file="logo-insa.png")
    canvas.create_image(150, 100, image=img)
    canvas.pack(side=tk.BOTTOM, expand=tk.YES)

    PageAccueil.pack(expand=tk.YES)

    return PageAccueil
    
    
#-------------------------------Page Settings-----------------------------------------

def settings(root, base_frame,theme):
    OptionList=["Dark","Light"]

    clear_frame(base_frame)
    setting = tk.Frame(base_frame, bg=theme[0], bd=0, relief=tk.SUNKEN) 

    
    #titre
    titre = tk.Label(setting, text="Settings", font =("Ralewayl",40), bg=theme[0], fg=theme[1])
    titre.pack()
    vide = tk.Canvas(setting, bg = theme[0], bd=0, width=100, height=50, highlightthickness=0)
    vide.pack()
    
    #Selection Menu
    variable = tk.StringVar()
    variable.set("App Theme")
    opt = tk.OptionMenu(setting, variable, *OptionList)
    opt.config(font=('Helvetica', 12), bg=theme[0], fg=theme[1],highlightthickness=0)
    opt.pack()

    vide = tk.Canvas(setting, bg = theme[0], bd=0, width=100, height=50, highlightthickness=0)
    vide.pack()

    def callback(root, base_frame):
        t = variable.get()
        if t=="Dark":
            theme=["#233C5D","white"]
            clear_frame(base_frame)
            root.config(background=theme[0])
            settings(root, base_frame,theme)

        elif t=="Light":
            theme=["white","black"]
            clear_frame(base_frame)
            root.config(background=theme[0])
            settings(root, base_frame,theme)
        



    #Bouton Paramètres
    txt = tk.StringVar()
    home_page = tk.Button(setting, textvariable=txt,padx = 34 , pady = 20, command=lambda:page1(root,base_frame,theme),bg=theme[0], fg=theme[1], font="Raleway")
    txt.set("Home menu")
    home_page.pack()
    vide = tk.Canvas(setting, bg = theme[0], bd=0, width=100, height=50, highlightthickness=0)
    vide.pack()
    #Bouton Paramètres
    txt = tk.StringVar()
    confirm = tk.Button(setting, textvariable=txt,padx = 34 , pady = 20, command=lambda:callback(root, base_frame),bg=theme[0], fg=theme[1], font="Raleway")
    txt.set("Confirm")
    confirm.pack(side=tk.LEFT)

    #Bouton Quitter
    txt = tk.StringVar()
    exit = tk.Button(setting, textvariable=txt,padx = 52 , pady = 20, command=root.destroy,bg=theme[0], fg=theme[1], font="Raleway")
    txt.set("Exit")
    exit.pack()
    setting.pack(expand=tk.YES)

    base_frame.pack(expand=tk.YES)
    
#-------------------------------Page Recommandation-----------------------------------------        

def recommandation(root, base_frame,theme):
    
    clear_frame(base_frame)
    frame=tk.Frame(base_frame, bg=theme[0], bd=0, relief=tk.SUNKEN)
    #titre
    titre = tk.Label(frame, text="Recommandation", font =("Ralewayl",40), bg=theme[0], fg=theme[1])
    titre.pack()
    vide = tk.Canvas(frame, bg = theme[0], bd=0, width=100, height=50, highlightthickness=0)
    vide.pack()
    txt = tk.StringVar()
    home_page = tk.Button(frame, textvariable=txt,padx = 34 , pady = 20, command=lambda:page1(root,base_frame,theme),bg=theme[0], fg=theme[1], font="Raleway")
    txt.set("Home menu")
    home_page.pack()
    vide = tk.Canvas(frame, bg = theme[0], bd=0, width=100, height=50, highlightthickness=0)
    vide.pack()
    frame.pack(expand=tk.YES)

#-------------------------------Page Recommandation-----------------------------------------        

def word_embedding(root, base_frame,theme):
    
    clear_frame(base_frame)
    frame=tk.Frame(base_frame, bg=theme[0], bd=0, relief=tk.SUNKEN)
    #titre
    titre = tk.Label(frame, text="Word Embedding", font =("Ralewayl",40), bg=theme[0], fg=theme[1])
    titre.pack()
    vide = tk.Canvas(frame, bg = theme[0], bd=0, width=100, height=50, highlightthickness=0)
    vide.pack()
    txt = tk.StringVar()
    home_page = tk.Button(frame, textvariable=txt,padx = 34 , pady = 20, command=lambda:page1(root,base_frame,theme),bg=theme[0], fg=theme[1], font="Raleway")
    txt.set("Home menu")
    home_page.pack()
    vide = tk.Canvas(frame, bg = theme[0], bd=0, width=100, height=50, highlightthickness=0)
    vide.pack()
    frame.pack(expand=tk.YES)

##-------------------------------App----------------------------------------- 

def app():
    #fonction qui permet de lancer l'application

    #Création d'une première fenêtre
    root = tk.Tk()
    theme = ["#233C5D","white"]
    #personnalisation de la fenetre
    root.title("MovieRecommandation")
    root.geometry("1080x720")                   #taille initiale de la page
    root.minsize(1080,640)                      #taille minimum de la fenetre
    root.iconbitmap("movies.ico")               #icone
    root.config(background=theme[0])
    fraame = tk.Frame(root)
    page1(root, fraame,theme)
    fraame.pack()
    root.mainloop()

##-------------------------------Main----------------------------------------- 

app()