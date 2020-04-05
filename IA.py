import sys
import re
import random
from random import choice, shuffle
from copy import deepcopy
from operator import itemgetter

class Bateau:

    def __init__(self,liste):

        self.name = name
        self.largeur = largeur
        self.longueur = longueur
        self.hauteur = hauteur
        self.position = []
        
        #pour l'IA
        self.cible = False

    
    #Bateau
    
        liste.extend(
                        [
                            Bateau("PorteContainer",5,2,0),
                            Bateau("PorteAvion",5,1,0),
                            Bateau("PorteAvion2",5,1,0),       
                            Bateau("Destroyer",4,1,0),   
                            Bateau("Destroyer2",4,1,0),
                            Bateau("Destroyer3",4,1,0),
                            Bateau("Torpilleur",3,2,0),
                            Bateau("Torpilleur2",3,2,0),
                            Bateau("Torpilleur3",3,2,0),
     #Sous-Marins                       
                            Bateau("SMnucleaire",6,1,random.randrange(3)),
                            Bateau("SMnucleaire1",6,1,random.randrange(3)),
                            Bateau("SMpetit",6,1,random.randrange(3)),
                            Bateau("SMpetit2",6,1,random.randrange(3)),
                            Bateau("SMpetit3",6,1,random.randrange(3)),
                            Bateau("SMmini",6,1,random.randrange(3)),
                            Bateau("SMmini2",6,1,random.randrange(3)),
                            Bateau("SMmini3",6,1,random.randrange(3)),
                         
                        ]
                    )
        
        for Bateau in liste:
            placement_bateau(self.largeur, self.longueur)
  
        

        
    def placement_bateau(self,largeur,longueur):
       
        #place le bateau sur le plateau
        mylist = [largeur,longueur]
        orientedboat = orientation_bateau(mylist[largeur,longueur])
        
        #position de base random
        x = random.randrange (1,15-orientedboat[0])
        y = random.randrange (1,15-orientedboat[1])
        
        x_temp = 1
        y_temp = 1
        for x_temp in  x:
            for y_temp in y:
                print("x")
        
        
    
        
    def orientation_bateau(self,mylist[largeur,longueur]):
    
        #change ou non l'orientation du bateau
        
        random.shuffle(mylist)
        
        return mylist[]
    
    def tirer(self,cible):
        if
        if cible == False:
            positionTir = [random.randint(0,14),random.randint(0,14)]
            
        else:


