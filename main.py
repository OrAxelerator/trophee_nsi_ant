import random
from cellule import get_cellule
from world import espace, LARGEUR, HAUTEUR
from draw import draw
from read_world import read_world
from chose2_0 import think
from unlock import unblock
from parametre import ant_array
from chose_cellule import choose
from backToHome2_0 import back_home
ant1 = {
    "pos" : [0,0],
    "angle" : [0,1],
    "have_food": False
}
#ant_array = [ant1]#TEST
print(ant_array)
hill = {
    "pos" : [0,0]
}

def move(choix:tuple, ant:dict):
    print("choix de move() : ", choix)
    #print("ant[pos] : ", ant["pos"])
    pheromones(espace, ant)
    #espace[ant["pos"][0]][ant1[1]] = 0
    #espace[ant1["pos"][0]][ant1["pos"][1]] += 1
    ant["pos"][0] += choix[0] 
    ant["pos"][1] += choix[1]
    print("angle : ", ant["angle"])

def pheromones(espace, ant:dict):
    """pose phéromones a la position de la fourmi avant son déplacement
    seulement si elle a de la nourriture"""
    if ant["have_food"]:
        print("pos :", espace[ant["pos"][0]][ant["pos"][1]])
        if espace[ant["pos"][0]][ant["pos"][1]] not in ("f","h") :
            espace[ant["pos"][0]][ant["pos"][1]] += 1 

print("LANCEMENT =========================================================================== ")
FOOD = 0
while True:
    res = input()
    if res == "q":
        print(f"FOOD recup durant simu: {FOOD}")
        break
    
    for ant in ant_array:
        if ant["have_food"]:
            print("ANT A DE LA 🍔🍔🍔🍔🍔🍔🍔")
            # if ant["pos"] == hill: # si sur la fourmilière
            if ant["pos"] != hill:
                nb_tour = 0 if read_world(ant, (0,0), espace) == "f" else 1 # Si sur "f" alors nb_tour = 1
                case = back_home(ant, hill, espace, nb_tour)

                move(case, ant) 
                if ant["pos"] == hill["pos"]:
                    FOOD +=1
                    print("ANT DEPOSE NOURITURE 🚗")
                    ant["have_food"] = False
                    print("BEFORE🚂🚂🚂🚂", ant["angle"])
                    ant["angle"] = (-(ant["angle"][0]), -(ant["angle"][1]))
                    print("AFTER 🧭🧭🧭🧭: ", ant["angle"])
            
        else: 
            print("--------------------------------------------------------------------")
            choix = get_cellule(espace,ant, "filtered") # choix "légal"
            print("CHOIIIIIIIIIIIIIIIIIIIIIIX", choix)
            if choix == [] :
                ant["angle"] = unblock(espace, ant)
                choix = get_cellule(espace, ant, "filtered")
                print("CHOIIIIIIIIIIIIIIIIIIIIIIX (nouveau)", choix)

            #print("tout les choix", choix)
            brain_fourmi = think(choix, ant, espace)
            print("brain : ", brain_fourmi)#devrait sortir que 1 ELEMENT
            move(brain_fourmi, ant)
            #
            #if food(choix, ant) != False and ant["have_food"] == False:
            #    print("ant have food")
            #    move(food(choix, ant), ant)#allez a nour
            #else:
            #    print("ant pas de food")
            #    dir = choose(choix, ant)
            #    print(dir)
            #    move(dir, ant)
    draw(espace, ant_array)
    print("----------------")
        #move(choix, ant)
        #espace[ant["pos"][0]][ant["pos"][1]] = "F"
        #draw(espace)
        #print("============")
        #input("...")

print(ant_array)