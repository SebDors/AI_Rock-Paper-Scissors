import random
import openpyxl
import numpy as np
import AIModel
Actions = ["Rock", "Paper", "Scissors"]
Resultat = ""


def Game(ChoixJoueur, UserPoint, RobotPoint):
    """
    Simulate a single round of the Rock-Paper-Scissors game and update the game results.

    Parameters:
        ChoixJoueur (str): The player's choice among "Rock", "Paper", or "Scissors".
        UserPoint (int): The current score of the player.
        RobotPoint (int): The current score of the robot.

    Returns:
        tuple: A tuple containing four values:
            - Resultat (str): The result of the game, can be "Won !", "Lost !", or "Draw !".
            - UserPoint (int): Updated score of the player after the round.
            - RobotPoint (int): Updated score of the robot after the round.
            - RobotChoice (str): The robot's choice among "Rock", "Paper", or "Scissors".
    """
    Actions = ["Rock", "Paper", "Scissors"]
    # Select RobotChoice between "Actions"
    RobotChoice = random.choice(Actions)

    # Checking the result of the game
    if ChoixJoueur == RobotChoice:
        Resultat = "Draw !"
    elif ChoixJoueur == "Rock" and RobotChoice == "Scissors":
        Resultat = "Won !"
        UserPoint += 1
    elif ChoixJoueur == "Paper" and RobotChoice == "Rock":
        Resultat = "Won !"
        UserPoint += 1
    elif ChoixJoueur == "Scissors" and RobotChoice == "Paper":
        Resultat = "Won !"
        UserPoint += 1
    else:
        RobotPoint += 1
        Resultat = "Lost !"

    JoueurNumber, RobotNumber, Resultatnumber = Switch(ChoixJoueur, RobotChoice, Resultat)
    MaJExcel(JoueurNumber, RobotNumber, Resultatnumber)

    return Resultat, UserPoint, RobotPoint, RobotChoice


def MaJExcel(ChoixJoueur, RobotChoice, Result):
    """
    Update the Excel file 'ResultatParties.xlsx' with the game results.

    Parameters:
        ChoixJoueur (int): Numerical representation of the player's choice (0 for Rock, 1 for Paper, 2 for Scissors).
        RobotChoice (int): Numerical representation of the robot's choice (0 for Rock, 1 for Paper, 2 for Scissors).
        Result (int): Numerical representation of the game result (0 for Robot Lost, 1 for Robot Won, 2 for Draw).

    Returns:
        None: The function does not return anything.
    """
    # Open Excel file
    classeur = openpyxl.load_workbook("ResultatParties.xlsx")
    Paper = classeur.active

    # Updating data
    Paper.append([ChoixJoueur, RobotChoice, Result])
    classeur.save("ResultatParties.xlsx")


def Switch(JoueurToSwitch=None, RobotToSwitch=None, ResultatToSwitch=None):
    """
    Convert the input choices and result into corresponding numerical representations.

    Parameters:
        JoueurToSwitch (str): The player's choice among "Rock", "Paper", or "Scissors".
        RobotToSwitch (str): The robot's choice among "Rock", "Paper", or "Scissors".
        ResultatToSwitch (str): The result of the game, can be "Won !", "Lost !", or "Draw !".

    Returns:
        tuple: A tuple containing three integer values:
            - JoueurSwitched (int): Numerical representation of the player's choice (0 for Rock, 1 for Paper, 2 for Scissors).
            - RobotSwitched (int): Numerical representation of the robot's choice (0 for Rock, 1 for Paper, 2 for Scissors).
            - Switched (int): Numerical representation of the game result (0 for Robot Lost, 1 for Robot Won, 2 for Draw).
    """
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
        case "Won !":
            Switched = 0  # Robot Lost
        case "Lost !":
            Switched = 1  # Robot Won
        case "Draw !":
            Switched = 2  # Draw
    return JoueurSwitched, RobotSwitched, Switched

def Game2(ChoixJoueur, UserPoint, RobotPoint):
    ChoixJoueur = Switch(ChoixJoueur)
    RobotChoice = AIModel.predict_robot_choice(ChoixJoueur)
    if ChoixJoueur == RobotChoice:
        Resultat = "Draw !"
    elif ChoixJoueur == 0 and RobotChoice == 2:  # Pierre contre Ciseaux
        Resultat = "Won !"
        UserPoint += 1
    elif ChoixJoueur == 1 and RobotChoice == 0:  # Feuille contre Pierre
        Resultat = "Won !"
        UserPoint += 1
    elif ChoixJoueur == 2 and RobotChoice == 1:  # Ciseaux contre Feuille
        Resultat = "Won !"
        UserPoint += 1
    else:
        RobotPoint += 1
        Resultat = "Lost !"
    
    JoueurNumber, RobotNumber, Resultatnumber = Switch(ChoixJoueur, RobotChoice, Resultat)
    MaJExcel(JoueurNumber, RobotNumber, Resultatnumber)
    return Resultat, UserPoint, RobotPoint, RobotChoice

