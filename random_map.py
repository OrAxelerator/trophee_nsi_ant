import random
#from trophee_nsi_ant.draw import draw



    
def random_map(y:int, x:int, weightPath:float, weightObstacle:float) :
    """
    Docstring pour random_map
    
    :param y: Description
    :param x: Description
    :param weightPath: Description
    :param weightObstacle: Description
    """
    choix = [0,"X"]


    espace = []
    height = x
    width = y

    for i in range(height):
        row = []
        for loop in range(width):
            ch = random.choices(
                population=choix,
                weights=[weightPath, weightObstacle],
                k=1
                )
            row.append(ch[0])
            
        espace.append(row)
    
    #var = random.randint(0, height)
    
    
    espace[random.randint(0, height-1)][random.randint(0, width-1)] = "f"
    #espace[random.randint(0, height-1)][random.randint(0, width-1)] = "h"

    return espace


