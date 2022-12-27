import time
from random import random

class Cellule:
    def __init__(self):
        """
       Initialisation des attributs de la classe Cellule:
        """
        self.__actuel = False
        self.__futur = False
        self.__voisins = None
    def est_vivant(self):
        """
        Retourne l'état de la cellule
        param : 
                None
        return : 
                actuel (bool): l'état de la cellule actuel """

        return self.__actuel
    
    def set_voisins (self,l):
        """
        Affecter comme voisins la liste passée en paramètre
        param : 
                l (list): liste de voisins
        return :
                None
        """
        self.__voisins = l
    
    def get_voisins(self):
        """
        Renvoie la liste de voisins de la cellule
        param:
                None
        return :
                voisins (list) : liste de voisins
        """
        return self.__voisins

    def naitre(self):
        """
        Met l'état futur de la cellule à True
        param :
                None
        return :
                None
        """
        self.__futur = True
    def mourir(self):
        """
        Met l'état futur de la cellule à False
        param :
                None
        return :
                None
        """
        self.__futur = False
    
    def basculer(self):
        """
        Passe l'état futur de la cellule dans l'état actuel
        param :
                None
        return :
                None
        """
        self.__actuel= self.__futur

    def __str__(self):
        """
        Affiche une croix (X) si la cellule est vivante et un tiret (-) sinon 
        param :
                None
        return :
                affiche (str) 
        """
        if self.__actuel == True:
            affiche = "X"
        else:
            affiche = "-"
        return affiche 
    

    def calcule_etat_futur(self):
        """
        Permet d'implémenter les règles d'évolution du jeu de la vie 
        en préparant l'état futur à sa nouvelle valeur

        param :
                None
        return :
                None
        """
        cellules_vivantes = 0
        for i in self.__voisins:
            if i.est_vivant() == True:
                cellules_vivantes += 1
       
        if (cellules_vivantes != 2) and\
        (cellules_vivantes != 3) and\
        self.est_vivant():
            self.mourir()
        elif (cellules_vivantes == 3) and\
        not self.est_vivant():
            self.naitre()
        else:
            self.__futur = self.__actuel







class Grille:
    def __init__(self,largeur,hauteur) :
        self.largeur = largeur
        self.hauteur = hauteur
        self.matrix = [[Cellule() for i in range(self.largeur)]
                   for j in range(self.hauteur)]

    def dans_grille(self,i,j):
        """
        Vérifie que le point de coordonnées (i,j) est dans la grille
        param :
                i (int) : coordonnée de l'abscisse
                j (int) : coordonnée de l'ordonnée
        return :
                bool : True si le point est dans grille, sinon False
        """
        if i >= 0 and j>=0 and i<self.hauteur and j<self.largeur:
            return True
        else:
            False


    def set_XY(self,i,j,new_cell):
        """
        Permet d’affecter une nouvelle cellule à la case (i,j) de la grille,
        si (i,j) est bien dans la grille
        param : 
                i (int) : coordonnée de l'abscisse
                j (int) : coordonnée de l'ordonnée
                new_cell (int) : une nouvelle cellule
        return :
                None
        """
        if self.dans_grille(i,j):
            self.matrix[i][j] = new_cell
        else:
            raise IndexError(" le point (i,j) ne sont pas dans la grille")

    def get_XY(self,i,j):
        """
        Récupère la valeur situé aux coordonées (i,j) dans la grille
        param :
                i (int) : coordonnée de l'abscisse
                j (int) : coordonnée de l'ordonnée
        return :
                la valeur située aux coordonnées (i,j) : (Cellule)
        """
        if self.dans_grille(i,j):
            return self.matrix[i][j]
        else:
            raise IndexError(" le point (i,j) ne sont pas dans la grille")
        
    
    def get_largeur(self):
        """
        Permet de récupérer la largeur de la grille
        param :
                None
        return :
                largeur (int) : la largeur de la grille 
        """
        return self.largeur

    def get_hauteur(self):
        """
        Permet de récupérer la hauteur de la grille
        param :
                None
        return :
                 hauteur (int) : la hauteur de la grille 
        """
        return self.hauteur

    @staticmethod
    def est_voisin(i,j,x,y):
        """
        Méthode statique qui vérifie si les cases (i,j) et (x,y) sont voisines dans la grille.
        param :
                i (int) :  coordonnée de l'abscisse du point (i,j)
                j (int) : coordonnée de l'ordonnée du point(i,j)
                x (int) : coordonnée de l'abscisse du point (x,y)
                y (int) : coordonnée de l'ordonnée du point(x,y)

        return :
                bool
        """
        return (abs(x-i)==1) or (abs(y-j) == 1)
    
    def get_voisins(self,x,y):
        """
        Renvoie la liste des voisins d’une cellule
        param :
                x (int) : coordonnée de l'abscisse du point (x,y)
                y (int) : coordonnée de l'ordonnée du point(x,y)

        return :
                voisins (list) : liste de voisins
        """
        voisins = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if self.dans_grille(i, j) and\
                Grille.est_voisin(i,j,x,y):
                    voisins.append(self.get_XY(i, j))
        return voisins

    def affecte_voisins(self):
        """
        Affecte à chaque cellule de la grille la liste de ses voisins.
        param :
                None
        return :
                None
        """
        for i in range(self.hauteur):
            for j in range(self.largeur):
                val = self.get_XY(i,j)
                val.set_voisins(self.get_voisins(i,j))


    def __str__(self):
        """
        Affiche la grille sur un terminal
        param :
                None
        return :
                affiche (str)
        """
        affiche = ""
        for i in range(self.hauteur):
            for j in range(self.largeur):
                affiche += str(self.get_XY(i, j)) + " "
            affiche += "\n"
        return affiche


    def remplir_alea(self, taux):
        """
        Remplit aléatoirement la Grille avec un
        certain taux de Cellule vivantes

        param :
                taux (int)
        return :
                None
        """
        t = taux/100
        for i in range(self.hauteur):
            for j in range(self.largeur):
                r = random()
                if t >= r:
                    cellule = self.get_XY(i,j)
                    cellule.naitre()
                    cellule.basculer()

    def jeu(self):
        """
        Permet de passer en revue toutes les Cellules de 
        la Grille et de calculer leur état futur
        param :
                None
        return :
                None
        """
        for i in range(self.hauteur):
            for j in range(self.largeur):
                cellule = self.get_XY(i,j)
                cellule.calcule_etat_futur()

    def actualise(self)-> None:
        """
        Bascule toutes les cellules de la Grille dans leur état futur
        param :
                None
        return :
                None
        """
        for i in range(self.hauteur):
            for j in range(self.largeur):
                cellule = self.get_XY(i, j)
                cellule.basculer()

if __name__ == "__main__":
    def effacer_ecran():
        """
        Permet d'effacer l'écran dans un terminal
        param :
                None
        return :
                None
        """
        print("\u001B[H\u001B[J")


    grille = Grille(30,30)
    grille.remplir_alea(50)
    grille.affecte_voisins()
    while True:
        effacer_ecran() 
        print(grille)
        print("\n")
        time.sleep(0.5)
        grille.jeu()
        grille.actualise()
    



    




    


    
