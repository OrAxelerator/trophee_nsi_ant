import random
from cellule import get_cellule
from world import espace

ant1 = { # exemple
    "pos" : [3,1],
    "angle" : (0, 1),
    "have_food" : True
}

anthill1 = {
    "pos" : [0,4]
}



def back_home (ant, anthill, espace) :
    print("----------------------------------------------------------------------------")
    home_vector =()
    coordonnee_home = anthill["pos"] # ou autre selon definition de la position de la fourmillère
    #while ... :
    Xhome_vector = coordonnee_home[1] - ant["pos"][1]
    Yhome_vector = coordonnee_home[0] - ant["pos"][0] 
    home_vector = (Yhome_vector, Xhome_vector)# echanger peut etre
    print("home", home_vector)
    choix_angle = [(0,1), (0,-1), (1,0), (-1,0)]
    posi_vector_angle = []

    for el in choix_angle : #verifie quels angles solution 
        ant["angle"] = el 
        choix = get_cellule(espace, ant)
        if choix != [] :
            posi_vector_angle.append(el)

    print("posi_vector_angle", posi_vector_angle)
    res = []
    angles = []
    good_angle = ()
    max_produit_scalaire = []
    max_angle = []

    for i, el in enumerate(posi_vector_angle) :
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
        max_angle.append(posi_vector_angle[el[1]]) # renvoie les vecteur dans posivector a la position du produit scalaire
    
    #print("max", max_produit_scalaire)
    #print("maximum choisi", posi_vector_angle[res.index(max(angles))]) #mauvais car 3 dans res et non 4 comme vector angle
    #max_angle = posi_vector_angle[res.index(max_produit_scalaire)]

    angle = random.choice(max_angle) #si plusieurs produit scalaire fait random  : a voir
    print("angleeeeeeeeeeeeeee", angle)
    
    ant["angle"] = angle # initialise pour la suite

    # posi_vector_direction = get_cellule(espace, ant)
    
    # if posi_vector_direction == [] :
    #     for el in max_angle :
    #         if el != angle :
    #             angle = el
        
    #     ant["angle"] = angle
    
    posi_vector_direction = get_cellule(espace, ant) # directions possibles en fonction de l'angle trouvé précedemment
    print("posi_vector_direction", posi_vector_direction)
    results = []
    #direction = []
    max_produit_scalaire_direction = []
    max_direction = []

    for i, el in enumerate(posi_vector_direction) :
        print("direction regardée", el)
        produit_scalaire = el[0] * home_vector[0] + el[1] * home_vector[1] #calcul le produit scalaire pour toute les directions
        print("produit_scalaire 11", produit_scalaire)
        results.append((produit_scalaire, i))

    maxi = results[0][0] #calcul du max
    for el in results :
        if el[0] > maxi :
            maxi = el[0]
    print("maxi2", maxi)
    for el in results :  #calcul si plusieurs max
        if el[0] == maxi :
            max_produit_scalaire_direction.append(el)

    for el in max_produit_scalaire_direction :
        max_direction.append(posi_vector_direction[el[1]]) # renvoie les directions auxquels les produits scalaires correspondes

    direction = random.choice(max_direction) #choisi au hasard
    print("directionnnnnnnnnnnnnnnnnnnnn", direction)


    return [angle, direction]

print(back_home(ant1, anthill1, espace))
        




