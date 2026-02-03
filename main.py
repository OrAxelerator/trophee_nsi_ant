import random
from cellule import get_cellule
from world import espace, LARGEUR, HAUTEUR
from draw import draw
import read_world

ant1 = [0, 6]

action = ("avancer", "droite", "gauche")


def avancer(p):
    return  [p[0] + 1, p[1]]

def droite(p):
    return  [p[0] + 1, p[1] + 1]

def gauche(p):
    return  [p[0] + 1, p[1] - 1]

def pos_ok(p):
    return 0<=p[0]<LARGEUR and 0<=p[1]<HAUTEUR


def move(choix, ant):
    espace[ant1[0]][ant1[1]] = 0
    espace[ant1["pos"][0]][ant1["pos"][1]] += 1
    ant1[0] += (choix[0])
    ant1[1] += (choix[1])
for l in range(20):
    choix = random.choice(get_cellule(espace, ant1))
    move(choix, ant1["pos"])
    espace[ant1["pos"][0]][ant1["pos"][1]] = "F"
    


    draw(espace)
    print("============")
    input("...")



