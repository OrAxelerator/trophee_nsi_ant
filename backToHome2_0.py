import random
from cellule import get_cellule
from world import espace
from read_world import read_world


ant1 = { # exemple
    "pos" : [3,1],
    "angle" : (0, 1),
    "have_food" : True
}

anthill1 = {
    "pos" : [0,4]
}

def maximumFero(choices, ant): # ANT
    maxFeroAngle = []
    choicesWithoutX = []
    for el in choices : 
        if read_world(ant, el, espace) != "X":
            choicesWithoutX.append(el)
    maximumTaux = read_world(ant, choicesWithoutX[0], espace)
    print("maximussssssssssssssssss", maximumTaux)
    for el in choicesWithoutX : 
        valFero = read_world(ant, el, espace)
        print("ferero rocher", valFero)
        if valFero == "X" :
            continue #skip itération de la boucle
        if valFero == "f" :
            valFero = 1
        print("valFero", valFero)
        print("maximumTaux", maximumTaux)
        if valFero > maximumTaux :
            maximumTaux = valFero
            print("Oh noooooooooooooooooooooooooooooooo")

    for el in choices :
        if read_world(ant, el, espace) == maximumTaux :
            maxFeroAngle.append(el)
    print("maximum de feomone sur l'angle", maxFeroAngle)
    return maxFeroAngle


def meilleurProduitScalaire(choix, ant, anthill) :
        home_vector = ()
        coordonnee_home = anthill["pos"] # ou autre selon definition de la position de la fourmillère
        #while ... :
        Xhome_vector = coordonnee_home[1] - ant["pos"][1]
        Yhome_vector = coordonnee_home[0] - ant["pos"][0] 
        home_vector = (Yhome_vector, Xhome_vector)

        res = []
        angles = []
        good_angle = ()
        max_produit_scalaire = []
        max_angle = []

        for i, el in enumerate(choix) :
            print("angle regardé", el)
            produit_scalaire = el[0] * home_vector[0] + el[1] * home_vector[1] #calcul vecteur de chaque angle
            print("produit_scalaire 11", produit_scalaire)
            #res.append(produit_scalaire)
            angles.append((produit_scalaire, i)) # stocke le produit scalaire avec la position de l'angle auquel il renvoie

        print("angles produit scalaire ", angles) 
        maxi = angles[0][0] # calcul le produit scalaire le plus élevé
        for el in angles :
            if el[0] > maxi :
                maxi = el[0]


        print("maxi", maxi)
        for el in angles : #regarde si plusieurs produits scalaire max
            if el[0] == maxi :
                max_produit_scalaire.append(el)

        print("max_produit_scalaire", max_produit_scalaire)
        for el in max_produit_scalaire :
            max_angle.append(choix[el[1]]) # renvoie les vecteur dans posivector a la position du produit scalaire

        return max_angle


def find(posi, ant, obs, anthill): 
    if obs == True : #si il y a un obstacle alors la fourmi fait en fonction des feros
        bestAngles = maximumFero(posi, ant) 
        if len(bestAngles) == 1 :
            choosedOne = bestAngles
        else :
            choosedOne = meilleurProduitScalaire(bestAngles, ant, anthill )
            
    elif obs == False :
        bestAngles = meilleurProduitScalaire(posi, ant, anthill)
        if len(bestAngles) == 1 :
            choosedOne = bestAngles
        else :
            choosedOne = maximumFero(bestAngles, ant)
    return choosedOne

def back_home (ant, anthill, espace, nb_tour) :
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    # while ant["pos"] != anthill["pos"] :
    angle_beginning = ant["angle"]
    print("----------------------------------------------------------------------------")

        

    print("Choice angle in process ....")
    choix_angle = [(0,1), (0,-1), (1,0), (-1,0)]
    posi_vector_angle = []
    obs = False
    angleXopposed = []

    for el in choix_angle : #verifie quels angles ont des solutions
            ant["angle"] = el 
            choix = get_cellule(espace, ant, mode = "all")
            for elm in choix :
                if read_world(ant, elm, espace) == "h" : 
                    return elm
                elif read_world(ant, elm, espace) == "X" : 
                    obs = True
            if choix != [] :
                posi_vector_angle.append(el)
                if el != (-(angle_beginning[0]), -(angle_beginning[1])) :
                    angleXopposed.append(el)
                #regarde si obsatacle autour de la fourmi


    if nb_tour == 0 :
            possibliyGoodAngle = find(posi_vector_angle, ant, obs, anthill)

    elif nb_tour != 0 :
            possibliyGoodAngle = find(angleXopposed, ant, obs, anthill) #ajouter pas le droit prendre angle opposé sauf si obligé et sauf au début
            if possibliyGoodAngle == [] :
                possibliyGoodAngle = find(posi_vector_angle, ant, obs, anthill)

    ant["angle"] = random.choice(possibliyGoodAngle)
    print("Thanks for waiting, angle choosed is ", ant["angle"])
    print("Now, please wait, the choice of direction direction is in process...")
    posi_vector_direction = get_cellule(espace, ant, mode="filtered")
    directionChoosed = random.choice(find(posi_vector_direction, ant, obs, anthill))
    print("Thanks again, so the ant might go to ", directionChoosed)
        
        #nb_tour += 1
        
    print("POSITION",ant["pos"])
    return directionChoosed

        

#print("test",back_home(ant1, anthill1, espace, ))

            



    