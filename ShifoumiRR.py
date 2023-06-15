import time
import random
Actions = ["Pierre", "Feuille", "Ciseaux"]
Resultat = ""


def Game(ChoixJoueur, UserPoint, RobotPoint):
    RobotChoiceText = random.choice(Actions)

    if ChoixJoueur == RobotChoiceText:
        Resultat = "Match nul !"
    elif ChoixJoueur == "Pierre" and RobotChoiceText == "Ciseaux":
        Resultat = "Gagné !"
        UserPoint += 1
    elif ChoixJoueur == "Feuille" and RobotChoiceText == "Pierre":
        Resultat = "Gagné !"
        UserPoint += 1
    elif ChoixJoueur == "Ciseaux" and RobotChoiceText == "Feuille":
        Resultat = "Gagné !"
        UserPoint += 1
    else:
        RobotPoint += 1
        Resultat = "Perdu !"
    return Resultat, UserPoint, RobotPoint
