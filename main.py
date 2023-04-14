# Jeu de pendu by JulianoM8103
import random

mots = ["python", "pendu", "baguette", "coq", "france", "lunettes", "cube", "pierre", "gobelet", "lampe", "stylo", "stylos", "chat", "lupin", "posca", "feutre", "oiseau", "chien", "rat", "paris", "drapeau", "tour", "roue", "neige", "hiver", "printemps"]

mot = random.choice(mots)

nb_tentatives = 6

lettres_devinées = []

while nb_tentatives > 0:

    affichage = ""
    for lettre in mot:
        if lettre in lettres_devinées:
            affichage += lettre
        else:
            affichage += "-"
    print(affichage)

    lettre = input("Entrez une lettre : ")

    if lettre in mot:
        lettres_devinées.append(lettre)
        print("Bien joué !")
    else:
        nb_tentatives -= 1
        print("Raté ! Il vous reste", nb_tentatives, "tentatives.")

    if "-" not in affichage:
        print("Bravo, vous avez gagné ! Le mot était", mot)
        break

if nb_tentatives == 0:
    print("Dommage, vous avez perdu. Le mot était", mot)
