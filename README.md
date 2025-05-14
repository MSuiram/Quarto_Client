#Bot Quarto
===========

Ce projet consiste à créer un algorithme pouvant jouer à Quarto. Pour cela, il comunique via réseau avec un autre projet Git Hub : https://github.com/qlurkin/PI2CChampionshipRunner

##Fonctionnement

Le Bot est un algorithme de type Negamax avec ABPruning limité dans le temps. C'est a dire qu'il joue au jeu tous seul au jeu pendant plusieurs tours jusqu'au moment où la limite de temps est dépasser. A ce moment là, il retounre le meilleur coups qu'il a pu calculer.

##Stratégie

L'Algorithme pouvant avoir plusieurs coup d'avance permet d'aller directement vers les états les plus favorable. Cela est due au calcule d'une heuristique donnant une valeur à cchaque états terminal de la parie.

Pour ce Bot, l'heuristique est égale à la somme des valeurs des différent lignes et les valeurs des lignes sont égale au nombre de caractérisiques présente sur tout les pièces de cette même ligne plus le nombre de pièce présent sur la ligne.
Cette heuristique n'est surement pas la meilleur.

Si il a une possibilité de gagner en possant sa pièce, il le fera directement à la place de commencer à calculer autre chose.

Au début de la partie, si le Bot est le premier joueurs, il présentera un pièce choisie aléatoirement.

##Bibliothèques utilisés

- **socket** : sert à communiquer via le réseau
- **random** : permet de faire des actions aléatoires
- **json** : permet d'utiliser des fichiés Json dans le projet
- **sys** : permet de comuniquer des informations avec l'ordinateur
- **time** : permet de gérer le temps
- **pytest** et **unittest** : permettent de faire des tests sur différentes partie du programe

##Utiliser le Bot

Pour utiliser le Bot, il vous faut deux chose:

1. Intaller les différentes bibliothèques utiliés et se trouvant dans le *requirements.txt*
2. Conaître l'adresse Ip et le Port du serveur

Puis, il vous suffira d'ouvrir un terminal et de taper:

`py client.py <IP> <Port>`