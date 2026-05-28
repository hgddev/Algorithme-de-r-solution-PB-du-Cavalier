#PHASE 1 : 

#Etape 1 du projet, Comprendre le problème et trouver une solution : 

#si la case est libre et que le mouvement est affectue alors mettre case apres mouv a 1 ou 2,3,4,5,6 jusqua 64 en ajoutant 1 a chaque mouv pour indiquer que la case est occupée
#le mouv va se faire tout seul en fonction de la position actuelle du cavalier et de la position de la case d'arrivée
#si le mouv est valide alors on met la case d'arrivée a 1 et on recommence le processus jusqu'à ce que le cavalier ait fait 64 mouvs et que toutes les cases soient occupées
#si le cavalier une fois arrivé sur une nouvelle case ne peut plus bouger alors on retourne a la case précédente et on essaye une autre direction de mouv
#le cavalier se deplace en L, c'est à dire 2 cases dans une direction et 1 case dans une direction perpendiculaire, ou 1 case dans une direction et 2 cases dans une direction perpendiculaire
#il faut creer une boucle qui va essayer tous les mouvs possibles pour le cavalier a partir de sa position actuelle, et pour chaque mouv valide, on incremente la case d'arrivée a 1 et on recommence le processus jusqu'à ce que le cavalier ait fait 64 mouvs ou qu'il ne puisse plus bouger
#si le cavalier ne peut plus bouger alors on retourne a la case précédente et on essaye une autre direction de mouv, et ainsi de suite jusqu'à ce que le cavalier ait fait 64 mouvs ou qu'il ne puisse plus bouger
#le cavalier peut etre bloqué si le prochain mouvement est hors champ ou si la case d'arrivée est occupée, il faut donc essayer une autre direction de mouv si le cavalier est bloqué
#le cavalier peut se deplacer dans 8 directions différentes, il faut donc creer une liste de ces directions et les essayer une par une pour chaque position du cavalier
#le cavalier peut se deplacer dans les directions suivantes : (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)
#il faut donc creer une liste de ces directions et les essayer une par une pour chaque position du cavalier, en utilisant la fonction estValide pour vérifier si le mouvement est valide ou non, et en utilisant une boucle pour essayer tous les mouvements possibles jusqu'à ce que le cavalier ait fait 64 mouvs ou qu'il ne puisse plus bouger
#declaration grille de 8x8 cases, initialisée à 0
#code de lalgorithme de backtracking pour trouver un chemin pour le cavalier qui visite toutes les cases de l'échiquier





#Phase 2 : Implémentation de l'Algorithme 

#PROTOTYPE 


#Objectif : Coder l'algorithme avec Backtracking.
# Coder la fonction de vérifcation : Écrire une fonction estValide(x, y) qui vérife si
#une case est dans les limites et n'a pas encore été visitée.
# Implémenter le Backtracking : Écrire la fonction récursive principale qui :
# Marque la case actuelle comme visitée.
# Vérife la condition d'arrêt (compteur = taille totale).
# Teste récursivement les mouvements possibles.
# Backtrack : Remet la case à 0 (non visitée) si le chemin mène à une impasse.
# Test initial : Valider l'algorithme sur un petit échiquier (5 × 5) pour éviter les temps de
#calcul trop longs lors du débogage.

import numpy as np

# Configuration
TAILLE = 5
echiquier = np.zeros((TAILLE, TAILLE), dtype=int)
# L'ordre de ces directions va déterminer si l'algo trouve vite... ou jamais.
directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

def est_valide(x, y):
    return 0 <= x < TAILLE and 0 <= y < TAILLE and echiquier[x][y] == 0

def backtracking(x, y, move_count):
    # Condition de victoire
    if move_count == TAILLE * TAILLE:
        return True

    # On essaie les directions "bêtement" dans l'ordre de la liste
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        
        if est_valide(nx, ny):
            echiquier[nx][ny] = move_count + 1
            
            if backtracking(nx, ny, move_count + 1):
                return True
            
            # Backtrack : on efface et on essaie la direction suivante
            echiquier[nx][ny] = 0
            
    return False

# --- LANCEMENT ---
start_x, start_y = 0, 4
echiquier[start_x][start_y] = 1

print("Calcul avec backtracking(5x5) : VEUILLEZ PATIENTER")

if backtracking(start_x, start_y, 1):
    print("CHEMIN HAMILTONIEN TROUVE !")
    for ligne in echiquier:
        print(" ".join(f"{val:2d}" for val in ligne))
else:
    print("Aucun chemin n'a été trouvé")