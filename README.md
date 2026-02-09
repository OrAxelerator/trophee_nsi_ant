# Trophee-NSI-ant
Programme confectionné par une équipe brillante préselectionnée par le `MIT`.

Ce projet vise à simuler les `déplacements` des fourmies d'une colonie pour trouver leur ``nourriture`` par le biais de ``phéromones`` laissées sur leur passage.

On retrouve différents ``fichiers sources`` :
- [``main``](main.py) : le fichier d'entrée du programme
- [``get-cellule``](cellule.py): permettant de voir les possibilités de déplacement d'une fourmi
- [``draw``](draw.py) : permettant un affichage épuré
- [``move``](main.py) : fichier qui simule les déplacements aléatoires des fourmies sur la map choisie
- [``food``](food.py) : avec juste la position d'une fourmi et ces déplacement possible elle detecte si elle à accès a de la nourriture ("f")

## Processus de la simulation 
Vous disposez de `plusieurs maps `monde à votre guise, à vous de choisir celle qui vous convient selon leur `typographie` que ce soit par rapports aux obstacles qu'elle présente, la taille de la carte etc... 

Les fourmies commencent la simulation en sortant de leur fourmilière. Elles ont alors la possiblité des créer des chemins pour 

---

Créer votre propre map depuis ce site : 
https://oraxelerator.github.io/trophee-nsi-ant/tools/index.html