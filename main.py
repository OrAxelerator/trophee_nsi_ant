import random
from cellule import get_cellule
from world import espace, LARGEUR, HAUTEUR
from draw import draw
import read_world
from parametre import ant_array


def avancer(p):
    return  [p[0] + 1, p[1]]

def droite(p):
    return  [p[0] + 1, p[1] + 1]

def gauche(p):
    return  [p[0] + 1, p[1] - 1]

def pos_ok(p):
    return 0<=p[0]<LARGEUR and 0<=p[1]<HAUTEUR




def move(choix, ant):
    pheromones(espace, ant)
    #espace[ant["pos"][0]][ant1[1]] = 0
    #espace[ant1["pos"][0]][ant1["pos"][1]] += 1
    print(choix)
    print(ant["pos"])
    ant["pos"][0] += choix[0][0]
    ant["pos"][1] += choix[1][1]


def pheromones(espace, ant):
    """pose phéromones"""
    if ant["have_food"]:
        espace[ant["pos"][0]][ant["pos"][1]] += 1 

from chose_cellule import choose

from food import food
for l in range(20):
    for ant in ant_array:
        print(ant)
        choix = (get_cellule(espace,ant))# choix "légal"
        if food(choix, ant) != False and ant["have_food"] == False:
            move(food(choix, ant))#allez a nour
        else:
            move(choose(choix, ant), ant)

        draw(espace)
        #move(choix, ant)
        #espace[ant["pos"][0]][ant["pos"][1]] = "F"
        #draw(espace)
        #print("============")
        #input("...")