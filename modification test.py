#########################################
# groupe MPCI 5
# Anthonin Le nevez
# Kaïs Cheboub
# Anessa Diallo
# Enzo Reale
# Phkar Romdoul
# https://github.com/uvsq-info/l1-python
#########################################

#importation
import tkinter as tk
import random, marshal


#creation de la fenetre
racine = tk.Tk()
racine.title("simulation incendie")
racine.resizable(height = 300, width = 300)


#Couleur
Bleu = "blue"
Vert = "green4"
Rouge = "red"
Jaune =  "yellow"
Gris = "grey30"
Noir = "grey1"

#Affichage
HEIGHT, WIDTH = 640, 640
haut_case= HEIGHT//80
larg_case = WIDTH//80
canvas = tk.Canvas(racine, bg="white", height = HEIGHT, width=WIDTH)
canvas.grid(columnspan=6, row=1)



#variable
Couleur=[Bleu, Vert, Rouge, Jaune, Gris, Noir]
Largeur, Hauteur = 80, 80
Terrain = 6400*[0]
NmbrTour = 0
auto = True
Durée = 6400*[0]

#constante
durée_feu = 3
durée_cendre = 3




#fonction

def aleatzone():
    #creation du terrain
    global Couleur, larg_case, haut_case, Terrain
    h = 0
    for i in range (80):
        for j in range (80):
            color = random.choice([Bleu, Vert, Jaune])
            Terrain[h] = color
            canvas.create_rectangle((i*larg_case, j*haut_case),
                ((i+1)*larg_case, (j+1)*haut_case), fill=Terrain[h])
            h +=1

def save():
    #Sauvegarde du terrain dans le fichier sauvegarde
    global Terrain
    k = 0
    with open("sauvegarde.txt", 'w') as filout :
        for i in range (80):
          for j in range (80):
            filout.write("{}\n".format(Terrain[k]))
            k += 1

def load():
    #Chargement du terrain a partir du fichier sauvegarde
    global Couleur, larg_case, haut_case, Terrain
    with open("sauvegarde.txt", 'r') as filin:
        for i in range (80):
          for j in range (80):
                canvas.create_rectangle((i*larg_case, j*haut_case),
                    ((i+1)*larg_case, (j+1)*haut_case), fill= filin.readline())


def suivant():
    #pour le parcour Pas à pas
    global Terrain, NmbrTour
    k = 0
    for i in range (80):
        for j in range (80):
            print(Terrain[k])
            if Terrain[k] == Rouge :
                Durée[k] -= 1
                if Durée[k] == 0 :
                    Terrain[k] = Gris
                    Durée[k] = durée_cendre
                    canvas.create_rectangle((i*larg_case, j*haut_case),
                        ((i+1)*larg_case, (j+1)*haut_case), fill=Terrain[k])
            elif Terrain[k] == Gris :
                Durée[k] -= 1
                if Durée[k] == 0 :
                    Terrain[k] = Noir
                    canvas.create_rectangle((i*larg_case, j*haut_case),
                        ((i+1)*larg_case, (j+1)*haut_case), fill=Terrain[k])
            elif Terrain[k] == Jaune :
                if Terrain[(i+1)+j*100] == Rouge or Terrain[(i-1)+j*100] == Rouge or Terrain[i+(j+1)*100] == Rouge or Terrain[i+(j-1)*100] == Rouge :
                    Terrain[k] = Rouge
                    Durée[k] = durée_feu
                    canvas.create_rectangle((i*larg_case, j*haut_case),
                        ((i+1)*larg_case, (j+1)*haut_case), fill=Terrain[k])
            elif Terrain[k] == Vert :
                proba = 0
                if Terrain[(i+1)+j*100] == Rouge :
                    proba += 0.1
                if Terrain[(i-1)+j*100] == Rouge :
                    proba += 0.1
                if Terrain[i+(j+1)*100] == Rouge :
                    proba += 0.1
                if Terrain[i+(j-1)*100] == Rouge :
                    proba += 0.1
                chance = random.random()
                if proba >= chance :
                    Terrain[k] = Rouge
                    Durée[k] = durée_feu
                    canvas.create_rectangle((i*larg_case, j*haut_case),
                        ((i+1)*larg_case, (j+1)*haut_case), fill=Terrain[k])
            k+=1
    NmbrTour +=1

def start():
    #Simulation automatique 
    global Terrain, auto
    auto = True

def stop():
    #arrêt de la simulation
    global Terrain, auto


def click(event):
    #Click qui transforme les forets et les plaines en feu
    global Terrain, Vert, Jaune, Rouge, larg_case, haut_case
    print(event.x, event.y)
    k = 0
    for i in range (80):
        for j in range (80):
            x = larg_case*i
            y = haut_case*j
            if x< event.x <x+larg_case and y< event.y <y+haut_case:
                if Terrain[k] == Vert or Terrain[k] == Jaune :
                    Terrain[k] = Rouge
                    canvas.create_rectangle((i*larg_case, j*haut_case),
                        ((i+1)*larg_case, (j+1)*haut_case), fill=Terrain[k])
            k += 1

""" def tour():
    global Terrain, durée_cendre, durée_feu, Durée, larg_case, haut_case, Couleur, auto
    if auto ==  True :
        k = 0
        for i in range (80):
            for j in range (80):
                print(Terrain[k])
                if Terrain[k] == Rouge :
                    Durée[k] -= 1
                    if Durée[k] == 0 :
                        Terrain[k] = Gris
                        Durée[k] = durée_cendre
                        canvas.create_rectangle((i*larg_case, j*haut_case),
                            ((i+1)*larg_case, (j+1)*haut_case), fill=Terrain[k])
                elif Terrain[k] == Gris :
                    Durée[k] -= 1
                    if Durée[k] == 0 :
                        Terrain[k] = Noir
                        canvas.create_rectangle((i*larg_case, j*haut_case),
                            ((i+1)*larg_case, (j+1)*haut_case), fill=Terrain[k])
                elif Terrain[k] == Jaune :
                    if Terrain[(i+1)+j*100] == Rouge or Terrain[(i-1)+j*100] == Rouge or Terrain[i+(j+1)*100] == Rouge or Terrain[i+(j-1)*100] == Rouge :
                        Terrain[k] = Rouge
                        Durée[k] = durée_feu
                        canvas.create_rectangle((i*larg_case, j*haut_case),
                            ((i+1)*larg_case, (j+1)*haut_case), fill=Terrain[k])
                elif Terrain[k] == Vert :
                    proba = 0
                    if Terrain[(i+1)+j*100] == Rouge :
                        proba += 0.1
                    if Terrain[(i-1)+j*100] == Rouge :
                        proba += 0.1
                    if Terrain[i+(j+1)*100] == Rouge :
                        proba += 0.1
                    if Terrain[i+(j-1)*100] == Rouge :
                        proba += 0.1
                    chance = random.random()
                    if proba >= chance :
                        Terrain[k] = Rouge
                        Durée[k] = durée_feu
                        canvas.create_rectangle((i*larg_case, j*haut_case),
                            ((i+1)*larg_case, (j+1)*haut_case), fill=Terrain[k])
                k+=1 """

#Commande
Createur = tk.Button(racine, width= 10, highlightbackground="#393B3B",text="Crée", font = ("helvetica", "30"), command= aleatzone)
    # un bouton qui génère un terrain au hasard avec des parcelles d’eau, de forêt et de prairie;
Save = tk.Button(racine, width= 10, highlightbackground="#393B3B",text="Save", font = ("helvetica", "30"), command= save) 
    # un bouton pour sauvegarder l’état du terrain dans un fichier;
Load = tk.Button(racine, width= 10, highlightbackground="#393B3B",text="Load", font = ("helvetica", "30"), command = load) 
    # un bouton pour charger un terrain depuis un fichier;
EtapeSuivante = tk.Button(racine, width= 10, highlightbackground="#393B3B",text="step", font = ("helvetica", "30"), command = suivant) 
    # un bouton permet d’effectuer une étape de simulation;
Start = tk.Button(racine, width= 10, highlightbackground="#393B3B",text="Start", font = ("helvetica", "30"), command = start) 
    # un bouton qui permet de démarrer une simulation;
Stop = tk.Button(racine, width= 10, highlightbackground="#393B3B",text="Stop", font = ("helvetica", "30"), command = stop) 
    # un bouton pour arrêter la simulation;

#Position des commades
Createur.grid(row= 3, column= 0) # positionnement du Createur
Save.grid(row= 3, column= 1) # positionnement du Save
Load.grid(row= 3, column= 2) # positionnement du Load
EtapeSuivante.grid(row= 3, column= 3) # positionnement de l'Etape suivante
Start.grid(row= 3, column= 4) # positionnement du Start
Stop.grid(row= 3, column= 5) # positionnement du Stop




#Boucle du code
canvas.bind("<Button-1>",click)




racine.mainloop()
 