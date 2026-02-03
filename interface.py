from random_map import random_map
map_choosen = []

while map_choosen != "created" or map_choosen != "random" :
    map_choosen = input("Do you want to create a random map or an already created one ?  (random/created) : ")
    if map_choosen == "random" :
        random_map()
    elif map_choosen == "created" :
        map_used = input("Which one do you want to use between : ")

