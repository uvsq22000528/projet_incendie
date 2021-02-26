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
Largeur, Hauteur = 8, 8
Terrain = []
NmbrTour = 0
first = 1

#constante
durée_feu = 3
durée_cendre = 2




#fonction

def aleatzone():
    #creation du terrain
    global Couleur, Largeur, Hauteur, Terrain, first
    k = 0
    if first == 1 :
        for i in range(0, WIDTH, Largeur):
            for j in range(0, HEIGHT, Hauteur):
                Terrain.append([i, j, random.choice([Bleu, Vert, Jaune]), 0])
                canvas.create_rectangle((i, j),
                    (i+Largeur, j+Hauteur), fill=Terrain[k][2])
                k += 1
        first = 0
    else :
        for i in range(0, WIDTH, Largeur):
            for j in range(0, HEIGHT, Hauteur):
                Terrain[k][0] = i
                Terrain[k][1] = j
                Terrain[k][2] = random.choice([Bleu, Vert, Jaune])
                Terrain[k][3] = 0
                canvas.create_rectangle((i, j),
                    (i+Largeur, j+Hauteur), fill=Terrain[k][2])
                k += 1

def save():
    #Sauvegarde du terrain dans le fichier sauvegarde
    global Terrain
    k = 0
    with open("sauvegarde.txt", 'w') as filout :
        for i in range(0, WIDTH, Largeur):
            for j in range(0, HEIGHT, Hauteur):
                filout.write("{}\n".format(Terrain[k][2]))
                k += 1

def load():
    #Chargement du terrain a partir du fichier sauvegarde
    global Couleur, larg_case, haut_case, Terrain
    with open("sauvegarde.txt", 'r') as filin:
        for i in range(0, WIDTH, Largeur):
            for j in range(0, HEIGHT, Hauteur):
                canvas.create_rectangle((i, j),
                        (i+Largeur, j+Hauteur), fill=filin.readline())


def suivant():
   #pour le parcour Pas à pas
    global Terrain, NmbrTour, WIDTH, HEIGHT, Largeur, Hauteur
    k = 0
    for i in range(0, WIDTH, Largeur):
        for j in range(0, HEIGHT, Hauteur):
            if Terrain[k][2] == Rouge :
                Terrain[k][3] -= 1
                if Terrain[k][3] == 0 :
                    Terrain[k][2] = Gris
                    Terrain[k][3] = durée_cendre
                    canvas.create_rectangle((i, j),
                        (i+Largeur, j+Hauteur), fill=Terrain[k][2])
            elif Terrain[k][2] == Gris :
                Terrain[k][3] -= 1
                if Terrain[k][3] == 0 :
                    Terrain[k][2] = Noir
                    canvas.create_rectangle((i, j),
                        (i+Largeur, j+Hauteur), fill=Terrain[k][2])
            elif Terrain[k][2] == Jaune :
                if Terrain[k+1][2] == Rouge or Terrain[k-1][2] == Rouge or Terrain[k+HEIGHT//Hauteur][2] == Rouge or Terrain[k-HEIGHT//Hauteur][2] == Rouge :
                    if Terrain[k+1][3] < durée_feu or Terrain[k-1][3] < durée_feu or Terrain[k+HEIGHT//Hauteur][3] < durée_feu or Terrain[k-HEIGHT//Hauteur][3] < durée_feu :
                        Terrain[k][2] = Rouge
                        Terrain[k][3] = durée_feu
                        canvas.create_rectangle((i, j),
                            (i+Largeur, j+Hauteur), fill=Terrain[k][2])
            elif Terrain[k][2] == Vert :
                proba = 0
                if Terrain[k+1][2] == Rouge :
                    if Terrain[k+1][3] < durée_feu :
                        proba += 0.1
                if Terrain[k-1][2] == Rouge :
                    if Terrain[k-1][3] == durée_feu :
                        proba += 0.1
                if Terrain[k+HEIGHT//Hauteur][2] == Rouge :
                    if Terrain[k+HEIGHT//Hauteur][3] < durée_feu :
                        proba += 0.1
                if Terrain[k-HEIGHT//Hauteur][2] == Rouge :
                    if Terrain[k-HEIGHT//Hauteur][3] < durée_feu :
                        proba += 0.1
                chance = random.random()
                if proba >= chance :
                    Terrain[k][2] = Rouge
                    Terrain[k][3] = durée_feu
                    canvas.create_rectangle((i, j),
                        (i+Largeur, j+Hauteur), fill=Terrain[k][2])
            k+=1
    NmbrTour +=1

def start():
    #Simulation automatique 
    global Terrain

def stop():
    #arrêt de la simulation
    global Terrain


def click(event):
    #Click qui transforme les forets et les plaines en feu
    global Terrain, Vert, Jaune, Rouge, larg_case, haut_case, durée_feu
    print(event.x, event.y)
    k = 0
    for i in range(0, WIDTH, Largeur):
        for j in range(0, HEIGHT, Hauteur):
            if i< event.x <i+Largeur and j< event.y <j+Hauteur:
                if Terrain[k][2] == Vert or Terrain[k][2] == Jaune :
                    Terrain[k][2] = Rouge
                    Terrain[k][3] = durée_feu
                    canvas.create_rectangle((i, j),
                        (i+Largeur, j+Hauteur), fill=Terrain[k][2])
            k += 1

            




#Commande
Createur = tk.Button(racine, width= 10, highlightbackground="#393B3B",text="Crée", font = ("helvetica", "30"), command= aleatzone)
    # un bouton qui génère un terrain au hasard avec des parcelles d’eau, de forêt et de prairie;
Save = tk.Button(racine, width= 10, highlightbackground="#393B3B",text="Save", font = ("helvetica", "30"), command= save) 
    # un bouton pour sauvegarder l’état du terrain dans un fichier;
Load = tk.Button(racine, width= 10, highlightbackground="#393B3B",text="Load", font = ("helvetica", "30"), command = load) 
    # un bouton pour charger un terrain depuis un fichier;
EtapeSuivante = tk.Button(racine, width= 10, highlightbackground="#393B3B",text="step", font = ("helvetica", "30"), command = suivant )
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
 