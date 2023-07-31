import PySimpleGUI as sg
import Shifoumi
from PIL import Image, ImageOps
import io

UserPoint = 0
RobotPoint = 0
Color = "#FFF"

# Créer la mise en page de l'interface graphique
layout = [
    [sg.Text(" "*72,background_color=Color), sg.Text('Adversaire :', justification="right",background_color=Color,text_color="black",font=13)],
    [sg.Text(" ",background_color=Color),
     sg.Image(filename="Images/rock.png", key="EnemyRock",background_color=Color),
     sg.Image(filename="Images/paper.png", key="EnemyPaper",background_color=Color),
     sg.Image(filename="Images/scissors.png", key="EnemyScissors",background_color=Color)],
    [sg.Text(" "*62,background_color=Color),sg.Text('          Score : 0/0', key='-DYNAMIC_TEXT-',font=16,background_color=Color,text_color="black")],
    [sg.Text(" "*72,background_color=Color),sg.Text("Votre choix : ",background_color=Color,text_color="black",font=13)],
    [sg.Button(image_filename="Images/rock.png", button_color=('white'), key="Rock", border_width=5),
     sg.Button(image_filename="Images/paper.png", button_color=('white'), key="Paper", border_width=5),
     sg.Button(image_filename="Images/scissors.png", button_color=('white'), key="Scissors", border_width=5)],
]

# Créer la fenêtre
window = sg.Window('Pierre Feuille Ciseaux', layout, finalize=True,background_color=Color)

# Changer la couleur du texte en fonction du résultat de la partie 
def CouleurText(Resultat):
    if Resultat == "Perdu !":
        window["-DYNAMIC_TEXT-"].update(f"{Resultat}   Points : {UserPoint}/{RobotPoint}", text_color='red')
    elif Resultat == "Gagné !":
        window["-DYNAMIC_TEXT-"].update(f"{Resultat}   Points : {UserPoint}/{RobotPoint}", text_color='green')
    else:
        window["-DYNAMIC_TEXT-"].update(f"{Resultat}   Points : {UserPoint}/{RobotPoint}", text_color='black')
# Réinitialiser la couleur des images
def ColorerRobotChoice(image_path):
    # Charger l'image
    image = Image.open(image_path)

    # Ajouter un contour rouge à l'image
    image_avec_contour = ImageOps.expand(image, border=5, fill='red')

    return image_avec_contour
# Mettre en évidence le choix du robot avec un contour en noir 
def ShowRobotchoice(RobotChoice):
    # Charger les images d'origine (sans contour)
    window["EnemyRock"].update(filename="Images/rock.png")
    window["EnemyPaper"].update(filename="Images/paper.png")
    window["EnemyScissors"].update(filename="Images/scissors.png")
    match RobotChoice:
        case "Rock":
            # Charger l'image "EnemyRock" avec le contour en rouge
            image_avec_contour = ColorerRobotChoice("Images/rock.png")
            image_bytes = io.BytesIO()
            image_avec_contour.save(image_bytes, format='PNG')
            window["EnemyRock"].update(data=image_bytes.getvalue())
        case "Paper":
            # Charger l'image "EnemyPaper" avec le contour en rouge
            image_avec_contour = ColorerRobotChoice("Images/paper.png")
            image_bytes = io.BytesIO()
            image_avec_contour.save(image_bytes, format='PNG')
            window["EnemyPaper"].update(data=image_bytes.getvalue())
        case "Scissors":
            # Charger l'image "EnemyScissors" avec le contour en rouge
            image_avec_contour = ColorerRobotChoice("Images/scissors.png")
            image_bytes = io.BytesIO()
            image_avec_contour.save(image_bytes, format='PNG')
            window["EnemyScissors"].update(data=image_bytes.getvalue())
# Réinitialiser la couleur des bordures des boutons de l'utilisateur
def ReinitialiserBoutons():
    window["Rock"].update(button_color=('white'))
    window["Paper"].update(button_color=('white'))
    window["Scissors"].update(button_color=('white'))

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Quitter'):
        break
    if event in ['Rock', 'Paper', 'Scissors']:
        Resultat, UserPoint, RobotPoint, RobotChoice = Shifoumi.Game(
                event, UserPoint, RobotPoint)
        ShowRobotchoice(RobotChoice)
        CouleurText(Resultat)
        ReinitialiserBoutons()
        window[event].update(button_color="blue")


window.close()
