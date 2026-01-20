from main import espace
ant1 = (0,0)


def get_cellule(world, tuple):
    choices = {
        "right" : (0,1),
        "down" :(-1,0),
        "left" :(0,-1),
        "up": (1,0)
        }
    
    res=[]
    if tuple[0] == 0:
        res.append(choices["up"])
        pass 
    if tuple[0] == len(world[0]) - 1 :
        res.appen(choices[ "down"])
        pass 
    if tuple[1] == 0 :
        res.append(choices["left"])
        pass 
    if tuple[1] == len(world[0]) - 1:
        res.append(choices["right"])
        pass 

    possibilite = []
    for el in res :
        print(el)
        if el not in choices:
            print("recup")
            possibilite.append(el)
        
    print("res : ", possibilite)

get_cellule(espace,ant1 )