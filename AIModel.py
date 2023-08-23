import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Fonction pour entraîner le modèle
def train_model():
        # Charger les données depuis le fichier Excel
    data = pd.read_excel('ResultatParties.xlsx')

    # Préparation des données
    X = data[['User', 'Result']]
    y = data['Robot']
    print(y)
    model = SVC(kernel='linear')
    model.fit(X, y)
    print("Entrainé !")
    return model

def Win_condition(choice):
    # Définir les règles de victoire en fonction du choix donné
    if choice == 0:  # Pierre
        return 1  # Feuille gagne contre Pierre
    elif choice == 1:  # Feuille
        return 2  # Ciseaux gagne contre Feuille
    elif choice == 2:  # Ciseaux
        return 0  # Pierre gagne contre Ciseaux

# Fonction pour prédire le choix optimal du robot
def predict_robot_choice(user_choice):
    model = train_model()
    choice_to_win = Win_condition(user_choice)
    robot_choice = model.predict([[user_choice, 1]])
    print(f"Choix de l'IA : {robot_choice} choix pour gagner : {choice_to_win}")
    return robot_choice[0]