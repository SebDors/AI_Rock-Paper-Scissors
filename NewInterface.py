import PySimpleGUI as sg
import Shifoumi
from PIL import Image, ImageOps
import io

UserPoint = 0
RobotPoint = 0
Color = "#FFF"

# Create the layout of interface
layout = [
    [sg.Text(" "*72,background_color=Color), sg.Text('Opponent :', justification="right",background_color=Color,text_color="black",font=13)],
    [sg.Text(" ",background_color=Color),
     sg.Image(filename="Images/rock.png", key="EnemyRock",background_color=Color),
     sg.Image(filename="Images/paper.png", key="EnemyPaper",background_color=Color),
     sg.Image(filename="Images/scissors.png", key="EnemyScissors",background_color=Color)],
    [sg.Text(" "*62,background_color=Color),sg.Text('          Score : 0/0', key='-DYNAMIC_TEXT-',font=16,background_color=Color,text_color="black")],
    [sg.Text(" "*72,background_color=Color),sg.Text("Your choice : ",background_color=Color,text_color="black",font=13)],
    [sg.Button(image_filename="Images/rock.png", button_color=('white'), key="Rock", border_width=5),
     sg.Button(image_filename="Images/paper.png", button_color=('white'), key="Paper", border_width=5),
     sg.Button(image_filename="Images/scissors.png", button_color=('white'), key="Scissors", border_width=5)],
]

# Creating window
window = sg.Window('Pierre Feuille Ciseaux', layout, finalize=True,background_color=Color)

def ColorText(Result):
    """
    Update the game result text with appropriate colors based on the outcome.

    Parameters:
        Result (str): The result of the game, can be "Won !", "Lost !", or "Draw !".

    Returns:
        None: The function does not return anything.

    This function updates the text in the window element with the key "-DYNAMIC_TEXT-". The text is updated
    with the provided game result and the current scores of the player and robot. The text color is set based
    on the outcome of the game:
    - If the result is "Lost !", the text color is set to red.
    - If the result is "Won !", the text color is set to green.
    - If the result is "Draw !", the text color is set to black.
    """
    if Result == "Lost !":
        window["-DYNAMIC_TEXT-"].update(f"{Result}   Points : {UserPoint}/{RobotPoint}", text_color='red')
    elif Result == "Won !":
        window["-DYNAMIC_TEXT-"].update(f"{Result}   Points : {UserPoint}/{RobotPoint}", text_color='green')
    else:
        window["-DYNAMIC_TEXT-"].update(f"{Result}   Points : {UserPoint}/{RobotPoint}", text_color='black')

def ColorerRobotChoice(image_path):
    """
    Add a red border to the given image.

    Parameters:
        image_path (str): The file path to the image that needs a red border.

    Returns:
        Image: The modified image with a red border.
    """
    # Upload imageResetButtons
    image = Image.open(image_path)
    # Add a border
    image_with_border = ImageOps.expand(image, border=5, fill='red')
    return image_with_border

# Highlight the choice of robot with a black outline
def ShowRobotchoice(RobotChoice):
    """
    Update the displayed image of the robot's choice with a red outline.

    Parameters:
        RobotChoice (str): The robot's choice among "Rock", "Paper", or "Scissors".

    Returns:
        None: The function does not return anything.
    """
# Load original images (without outlines)
    window["EnemyRock"].update(filename="Images/rock.png")
    window["EnemyPaper"].update(filename="Images/paper.png")
    window["EnemyScissors"].update(filename="Images/scissors.png")
    match RobotChoice:
        case "Rock":
            # Load "EnemyRock" image with red outline
            image_with_border = ColorerRobotChoice("Images/rock.png")
            image_bytes = io.BytesIO()
            image_with_border.save(image_bytes, format='PNG')
            window["EnemyRock"].update(data=image_bytes.getvalue())
        case "Paper":
            # Load "EnemyPaper" image with red outline
            image_with_border = ColorerRobotChoice("Images/paper.png")
            image_bytes = io.BytesIO()
            image_with_border.save(image_bytes, format='PNG')
            window["EnemyPaper"].update(data=image_bytes.getvalue())
        case "Scissors":
            # Load "EnemyScissors" image with red outline
            image_with_border = ColorerRobotChoice("Images/scissors.png")
            image_bytes = io.BytesIO()
            image_with_border.save(image_bytes, format='PNG')
            window["EnemyScissors"].update(data=image_bytes.getvalue())

# Reset user button border color
def ResetButtons():
    """
    Reset the color of the Rock, Paper, and Scissors buttons to white.

    Parameters:
        None: This function does not take any parameters.

    Returns:
        None: The function does not return anything.
    """
    window["Rock"].update(button_color=('white'))
    window["Paper"].update(button_color=('white'))
    window["Scissors"].update(button_color=('white'))

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Quitter'):
        break
    if event in ['Rock', 'Paper', 'Scissors']:
        #Sending and receiving the game's result. 
        Result, UserPoint, RobotPoint, RobotChoice = Shifoumi.Game2(
                event, UserPoint, RobotPoint)
        ShowRobotchoice(RobotChoice)
        ColorText(Result)
        ResetButtons()
        window[event].update(button_color="blue")


window.close()
