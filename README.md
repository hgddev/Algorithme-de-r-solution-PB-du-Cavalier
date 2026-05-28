# Exploration Algorithmique — Le Tour du Cavalier

[![Language](https://img.shields.io/badge/Language-C%20%2F%20C++-blue.svg)](https://developer.mozilla.org/fr/)
[![Theory](https://img.shields.io/badge/Th%C3%A9orie-Graphes%20%26%20Combinatoire-orange)](#)
[![Algorithm](https://img.shields.io/badge/Algorithme-DFS%20%26%20Backtracking-red)](#)

Réalisé par Hugo Davy et Marcel Ekia Diwanga (2026).

---

## Objectif du Projet

L'objectif de cette SAE est de resoudre le probleme classique du **Tour du Cavalier** : reussir a deplacer un cavalier sur un echiquier de maniere a fouler chaque case une et une seule fois. Ce projet lie la modelisation mathematique (theorie des graphes, chemins hamiltoniens) a l'implementation algorithmique d'une recherche en profondeur (DFS) avec mecanisme de rebroussement (*Backtracking*).

---

## Structure et Phases du Projet

Le developpement et l'analyse de ce projet s'articulent autour de 5 phases majeures :

### Phase 1 : Compréhension et Modélisation
* **Modélisation en Graphe :** Assimilation du probleme ou chaque case de l'echiquier represente un sommet et chaque deplacement legal en "L" constitue une arete.
* **Structure de Données :** Representation memoire via une matrice standard (ex: `int echiquier[8][8]`) ou `0` indique une case vide et `1..64` l'ordre chronologique de passage.
* **Vecteurs de Direction :** Definition des 8 deplacements relatifs possibles du cavalier dans des tableaux de constantes pour optimiser les iterations de mouvement.

### Phase 2 : Implémentation de l'Algorithme
* **Contrôle des Limites :** Code de la fonction `estValide(x, y)` verifiant que la coordonnee cible est dans les clous de la matrice et n'a pas encore ete exploree.
* **Moteur de Backtracking :** Conception de la fonction recursive principale (marquage de la case, verification de la condition d'arret, tests recursifs des 8 directions et reinitialisation de la case a `0` en cas d'impasse).
* **Prototypes de Tests :** Validation initiale de la logique sur une grille reduite $5 \times 5$ pour esquiver les temps de calcul trop longs lors de la phase de debogage.

### Phase 3 : Livrables et Cas Spécifiques
* **Cas 1 — Parcours Ouvert :** Recherche et affichage console/graphique d'un chemin hamiltonien simple depuis une case quelconque, applique notamment a la configuration de la **Figure 3** du sujet.
* **Cas 2 — Le Tour Fermé (Cycle) :** Modification des conditions restrictives de l'algorithme pour s'assurer que la $N$-ieme case finale permet de reboucler sur la case de depart. Validation sur grilles $6 \times 6$ et $8 \times 8$.

### Phase 4 : Analyse Mathématique et Extension
* **Analyse des Symétries :** Deduction logique de nouvelles solutions geometriques (rotations, effets miroirs) a partir des donnees de la Figure 3 sans relancer de calcul machine.
* **Étude des Cas Impossibles :** Demonstration de l'inexistence de solutions pour les formats restreints $3 \times 3$ et $4 \times 4$.

---

## Compétences Apprises & Validées

* **Algorithmique Graphes :** Maitrise des parcours de graphes, de la recursivite et de la gestion de l'arbre des choix par Backtracking.
* **Optimisation de Code :** Sensibilisation a l'explosion combinatoire et a la reduction de la complexite algorithmique.
* **Rigueur Scientifique :** Redaction de justifications mathematiques de couplage et de parite pour les cas impossibles.

---

## Organisation des Fichiers

* `/src` : Contient le code source de l'algorithme (fichiers `.c` ou `.cpp`).
* `/doc` : Contient le rapport d'analyse theorique (symetries, impossibilites) ainsi que les captures des solutions.

