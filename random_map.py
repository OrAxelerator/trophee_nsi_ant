import random
from draw import draw
    
def random_map() :
    choix = ("1","1","1","1","1","🪨")

    random.choice(choix)
    espace = []
    largeur = 12
    longueur = 12

    for i in range(largeur):
        ranger = []
        for loop in range(longueur):
            ch = random.choice(choix)
            ranger.append(ch)
        espace.append(ranger)
    
    return espace