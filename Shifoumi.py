import random
import openpyxl
import numpy as np
Actions = ["Rock", "Paper", "Scissors"]
Resultat = ""


def Game(ChoixJoueur, UserPoint, RobotPoint):
    RobotChoice = random.choice(Actions)

    if ChoixJoueur == RobotChoice:
        Resultat = "Match nul !"
    elif ChoixJoueur == "Rock" and RobotChoice == "Scissors":
        Resultat = "Gagné !"
        UserPoint += 1
    elif ChoixJoueur == "Paper" and RobotChoice == "Rock":
        Resultat = "Gagné !"
        UserPoint += 1
    elif ChoixJoueur == "Scissors" and RobotChoice == "Paper":
        Resultat = "Gagné !"
        UserPoint += 1
    else:
        RobotPoint += 1
        Resultat = "Perdu !"
    JoueurNumber, RobotNumber, Resultatnumber = Switch(
        ChoixJoueur, RobotChoice, Resultat)
    MaJExcel(JoueurNumber, RobotNumber, Resultatnumber)
    print("RobotChoice = ",RobotChoice)
    return Resultat, UserPoint, RobotPoint, RobotChoice

def MaJExcel(ChoixJoueur, RobotChoice, Result):
    """
    ChoixJoueur : 0-Rock 1-Paper 2-Scissors
    RobotChoice : 0-Rock 1-Paper 2-Scissors
    Result      : 0-Perdu  1-Gagné   2-Egalité (Résultat du point de vue du robot)
    """
    # Ouverture du fichier
    classeur = openpyxl.load_workbook("ResultatParties.xlsx")
    Paper = classeur.active

    # Ajouter les données
    Paper.append([ChoixJoueur, RobotChoice, Result])
    classeur.save("ResultatParties.xlsx")

    # Lecture et affichage des données excel
    donnees_excel = []
    for ligne in Paper.iter_rows(values_only=True):
        donnees_excel.append(list(ligne))
    tableau_numpy = np.array(donnees_excel)

def Switch(JoueurToSwitch, RobotToSwitch, ResultatToSwitch):
    match JoueurToSwitch:
        case "Rock":
            JoueurSwitched = 0
        case "Paper":
            JoueurSwitched = 1
        case "Scissors":
            JoueurSwitched = 2

    match RobotToSwitch:
        case "Rock":
            RobotSwitched = 0
        case "Paper":
            RobotSwitched = 1
        case "Scissors":
            RobotSwitched = 2

    match ResultatToSwitch:
        case "Gagné !":
            Switched = 0  # Le robot à perdu
        case "Perdu !":
            Switched = 1  # Le robot à gagné
        case "Match nul !":
            Switched = 2  # Egalité
    return JoueurSwitched, RobotSwitched, Switched