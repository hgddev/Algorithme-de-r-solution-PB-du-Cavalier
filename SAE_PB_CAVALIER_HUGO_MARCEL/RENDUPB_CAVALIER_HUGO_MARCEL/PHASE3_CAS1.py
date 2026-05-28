import numpy as np
import random


#configuration de la taille de l'echiquier
TAILLE = 8
echiquier = np.zeros((TAILLE, TAILLE), dtype=int)
#echiquier est un tableau de 8x8 rempli de 0, il va servir a enregistrer les positions du cavalier

#mouvements possibles du cavalier
directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

#tableau pour enregistrer les positions a 1 mouvement du point de départ, soit les positions d'arrivées
tab_position_finale = []

#fonction ets valide, on verifie que le cavalier ne sorte pas de l'echiquier
def est_valide(x, y):
    return 0 <= x < TAILLE and 0 <= y < TAILLE and echiquier[x][y] == 0


#fonction coups possibles, on verifie les mouvements possibles du cavalier et on les enregistre dans une liste
def coups_possibles(x, y):
    coups=[]
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if est_valide(nx, ny):
            coups.append((nx, ny))
    return coups
#dx et dy sont les mouvements possibles du cavalier
#x et y sont les positions actuelles du cavalier
#nx et ny sont les nouvelles positions du cavalier apres le mouvement
#append ajoute les positions possibles du cavalier dans la liste coups




#cette fonction va enregistrer les positions a 1 mouvement du point de départ pour que le cavalier revienne sur une des positions enregistrées
def backtracking(x, y, move_count):
    # Condition de victoire
    if move_count == TAILLE * TAILLE:
        return True
    

    coups = coups_possibles(x, y)
    random.shuffle(coups)
    coups.sort(key=lambda pos: len(coups_possibles(pos[0], pos[1])))
#sort trie les coups possibles du plus petit nombre de coups possibles au plus grand 
   
    for nx, ny in coups:
            echiquier[nx][ny] = move_count + 1
#echiquier[nx][ny] est le tableau
#ici on passe la position actuelle a un numéro de mouvement pour enregistrer le chemin du cavalier
            if backtracking(nx, ny, move_count + 1):
                return True
#si le mouvement esy valide on continue a enregistrer les mouvements suivants sinon on revient en arrière

            # Backtrack : on efface et on essaie la direction suivante
            else:
                echiquier[nx][ny] = 0
    return False

# --- LANCEMENT ---
start_x, start_y = 0, 7
#position de départ du cavalier
echiquier[start_x][start_y] = 1
#point de départ du cavalier Soit le numéro 1 dans le tableau echiquier

tab_position_finale = coups_possibles(start_x,start_y)


print("Calcul avec backtracking(8x8) : VEUILLEZ PATIENTER")

if backtracking(start_x, start_y, 1):
    print("CHEMIN HAMILTONIEN TROUVE !")
    for ligne in echiquier:
        print(" ".join(f"{val:2d}" for val in ligne))
else:
    print("Aucun chemin n'a été trouvé")


    