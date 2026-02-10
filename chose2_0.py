from cellule import get_cellule 
import random

from world import espace
from cellule import get_cellule
#from ..world import espace
from read_world import read_world

ant_test = {
      "pos" : [0,0],
      "angle" : (0,1),
      "have_food" : False
}
choix_fourmi = get_cellule(espace, ant_test)

def think(choix: list, ant: dict, espace:list) -> tuple: 

    """
    renvoi le chemin le 'plus optimisé' selon les phéromones
    si la fourmi n'as pas accés a de la nourriture.
    Sinon renvoi le chemin direct a la nourriture si il y en a
    """
    food_path = []
    pheromone_rate1 = []
    pheromone_rate = []
    choixXF = []
    TtChoix =[]
    TousRead_world = {}
    #print("choix : " , choix)

    for el in choix :
        TousRead_world[read_world(ant, el, espace)] = 0
    
    for el in choix :
            print("OUI",el, read_world(ant, el, espace))
            #TousRead_world[read_world(ant, el, espace)] += 1

    print("read_world :",TousRead_world)
        
    if "f" not in TousRead_world : 
        for el in choix : 
            choixXF.append(el)
            #print("choixXF : ",choixXF)
            #print("el-ajouté")
            pheromone_rate.append(read_world(ant, el, espace) / len(choixXF))
            
            #print("-----")
            #print(f'choixXf : {choixXF}')
            #print(f'phero : {pheromone_rate}')
            #print(best_cellule)


        best_cellule = random.choices(  
            population = choixXF,
            weights = pheromone_rate,
            k=1#longeur de la liste a return 
        )
        #print("xF")
        #print("best", best_cellule)

        return best_cellule[0] # best_cellule est une liste a un tupple, pour rvoyer jsute le tupple -> [0]

        
    elif "f" in TousRead_world :
        if ant["have_food"] == False:  
            for el in choix :
                #print("read_world",read_world(ant, el))
                if read_world(ant,el, espace) == "f" :
                    food_path.append(el) 
            #ant["angle"] = (-(ant["angle"][0]), -(ant["angle"][1])) #si sur food, prend direction inverse
            #print("Food Food Food")
            ant["have_food"] = True 
            #print("f/false")
            return random.choice(food_path) # tupple

        elif ant["have_food"] == True :
            for el in choix :
                TtChoix.append(el) # ajouter les coordonnées de f + voir les coordonnées
                #print("TTchoix:",TtChoix)
                if read_world(ant, el, espace) != "f" :
                    pheromone_rate1.append(read_world(ant, el, espace) / len(TtChoix))
                #print("pheromone_rate1", pheromone_rate1)
            
            for i in range(TousRead_world["f"]) :
                pheromone_rate1.append(1 / len(TtChoix))
            
            #print("pherromone",pheromone_rate1)
            #print("Ttchoix", TtChoix)
            best_cellule1 = random.choices(  
                population = TtChoix,
                weights = pheromone_rate1,
                k=1
            )
            #print("bestie", best_cellule1)

            #print("f/True")
            return best_cellule1[0]
        
        
            
print("think :",think(choix_fourmi, ant_test, espace)) 