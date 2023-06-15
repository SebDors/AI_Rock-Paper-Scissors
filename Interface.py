import PySimpleGUI as sg
import ShifoumiRR

UserPoint = 0
RobotPoint = 0
Background = "#D4F1F4"
# Define the layout
centered_layout = [
    [sg.Image(filename="Images/rock.png"), sg.Image(
        filename="Images/scissors.png"), sg.Image(filename="Images/paper.png")],
    [sg.Button("Pierre", key="Pierre", button_color=("black", Background)),
     sg.Text("", size=(19, 1), background_color=Background),
     sg.Button("Feuille", key="Feuille", button_color=("black", Background)),
     sg.Text("", size=(19, 1), background_color=Background),
     sg.Button("Ciseaux", key="Ciseaux", button_color=("black", Background))],
    [sg.Column([[sg.Text("Faites votre choix", size=(19, 1), key="output", text_color="black", background_color=Background)]],
               element_justification='center', background_color=Background)]
]

layout = [
    [sg.Column(centered_layout, element_justification='center',
               vertical_alignment='center', background_color=Background)]
]

# Create the window
window = sg.Window("Pierre-Feuille-Ciseaux", layout,
                   background_color=Background)

# Event loop
while True:
    event, values = window.read()

    # If the user closes the window or clicks "Exit", end the loop
    if event == sg.WIN_CLOSED:
        break

    # Handle button events
    match event:
        case "Pierre":
            Resultat, UserPoint, RobotPoint = ShifoumiRR.Game(
                "Pierre", UserPoint, RobotPoint)
        case "Feuille":
            Resultat, UserPoint, RobotPoint = ShifoumiRR.Game(
                "Feuille", UserPoint, RobotPoint)
        case "Ciseaux":
            Resultat, UserPoint, RobotPoint = ShifoumiRR.Game(
                "Ciseaux", UserPoint, RobotPoint)

    window["output"].update(f"{Resultat}   Points : {UserPoint}/{RobotPoint}")

    if Resultat == 'Perdu !':
        window["output"].update(text_color="red")
    elif Resultat == 'Gagné !':
        window["output"].update(text_color="green")
    else:
        window["output"].update(text_color="black")

# Close the window
window.close()
