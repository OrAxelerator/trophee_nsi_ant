import random
from cellule import get_cellule
from world import espace
from read_world import read_world
ant1 = { # exemple
    "pos" : (0, 0),
    "angle" : (0,1),
    "have_food" : False
}
choix = get_cellule(espace, ant1)
print(read_world(ant1, (0,0)))
print("choix : ", choix)
# ant, choix

def choose(espace, choix, ant):
    res = []
    for el in choix :
        #print(el, read_world(ant, el))
        res.append(read_world(ant, el) / len(choix))
        #print (res)

    #print("res:", res)
    el =  random.choices(
        population=choix,
        weights=res,
        k=1
    )
    return el

print(choose(espace, choix, ant1))