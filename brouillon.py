"""
class MainFrame(tk.Tk):
    #frame qui va contenir toutes les différentes pages
    #Ce qui va nous permettre de naviguer
    
    #Constructeur
    def __init__(self):
        
        self.root = tk.Tk()
        #personnalisation de la fenetre
        self.root.title("MovieRecommandation")
        self.root.geometry("1080x720")                   #taille initiale de la page
        self.root.minsize(1080,640)                       #taille minimum de la fenetre
        self.root.iconbitmap("movies.ico")               #icone
        self.root.config(background="#233C5D")
        
        container = tk.Frame()
        container.grid(row = 0,column = 0, sticky = 'nesw')
        
        self.id= tk.StringVar()
        self.id.set("1")
        self.listing = {}
        
        for i in (PageAccueil, Settings):
            #permet de naviguer entre les pages
            page_name = i.__name__
            frame = i(parent = container, controller = self)
            frame.grid(row=0, column=0, sticky= 'nsew')
            self.listing[page_name] = frame
            
        self.up_frame('PageAccueil')
        
    def up_frame(self, page_name):
        page = self.listing[page_name]
        page.tkraise()  


class PageAccueil(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        
        #creer des frames
        PageAccueil= tk.Frame(self, bg="#233C5D", bd=1)
        frame1 = tk.Frame(PageAccueil, bg="#233C5D", bd=1, relief=tk.SUNKEN) 
        frame2 = tk.Frame(PageAccueil, bg="#233C5D", bd=1) 
        frame3 = tk.Frame(PageAccueil, bg="#233C5D", bd=1) 

        #Textes 
        titre = tk.Label(frame1, text="Bienvenue sur blabla", font =("Ralewayl",40), bg="#233C5D", fg="white")
        titre.pack()

        soustitre = tk.Label(frame1, text="Développée par Waechter Thibaut", font =("Raleway",30), bg="#233C5D", fg="white")
        soustitre.pack()

        #Boutons
        #Bouton valider
        browse_txt = tk.StringVar()
        browse_btn = tk.Button(frame2, textvariable=browse_txt, padx = 50 , pady = 20, command=lambda:test1(), font="Raleway")
        browse_txt.set("Valider")
        browse_btn.pack(side= tk.LEFT)

        #Bouton annuler
        txt = tk.StringVar()
        browse_btn = tk.Button(frame2, textvariable=txt,padx = 49 , pady = 20, command=lambda:test2(), font="Raleway")
        txt.set("Annuler")
        browse_btn.pack()

        #Bouton Paramètres
        txt = tk.StringVar()
        browse_btn = tk.Button(frame3, textvariable=txt,padx = 34 , pady = 20, command=lambda:controller.up_frame("Settings"), font="Raleway")
        txt.set("Paramètres")
        browse_btn.pack(side= tk.LEFT)

        #Bouton Quitter
        txt = tk.StringVar()
        browse_btn = tk.Button(frame3, textvariable=txt,padx = 52 , pady = 20, command=self.destroy, font="Raleway")
        txt.set("Quitter")
        browse_btn.pack()
        vide = tk.Canvas(PageAccueil, bg = "#233C5D", bd=0, width=100, height=100, highlightthickness=0)


        #ajouter
        frame1.pack(expand=tk.YES)
        vide.pack(expand=tk.YES)
        frame2.pack(expand=tk.YES)
        frame3.pack(expand=tk.YES)
        PageAccueil.pack(expand=tk.YES)

        #création d'un canvas
        canvas = tk.Canvas(self, bg = "#233C5D", bd=0, width=300, height=200, highlightthickness=1)

        #logo
        photoimage = ImageTk.PhotoImage(file = "logo-insa.png")
        canvas.create_image(150, 100, image=photoimage)
        canvas.pack(side=tk.BOTTOM, expand= tk.YES)
        

class Settings(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.id = controller.id
        
        frame1 = tk.Frame(self, bg="#233C5D", bd=1, relief=tk.SUNKEN) 
        #Bouton Paramètres
        txt = tk.StringVar()
        browse_btn = tk.Button(frame1, textvariable=txt,padx = 34 , pady = 20, command=lambda:controller.up_frame("PageAccueil"), font="Raleway")
        txt.set("Menu Principale")
        #Bouton Quitter
        txt = tk.StringVar()
        browse_btn = tk.Button(frame1, textvariable=txt,padx = 52 , pady = 20, command=self.destroy, font="Raleway")
        txt.set("Quitter")
        browse_btn.pack()
        frame1.pack(side= tk.LEFT)
"""