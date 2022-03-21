import PySimpleGUI as sg
import random, time
sg.theme("LightBlue")


layout=[[sg.Text("Enter a number out of 50",font='Lucida'), sg.InputText(key='-PROGRESS_VALUE-', font='Lucida, 20', size=(20, 40))],
        [sg.ProgressBar(50, orientation='h', size=(100, 20), border_width=4, key='-PROGRESS_BAR-', bar_color=("Blue","Yellow"))],
        [sg.Button('Change Progress'), sg.Exit()]]

window =sg.Window("Progress Bar",layout)


while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
                break
    if event == "Change Progress":
        progress_value = int(values['-PROGRESS_VALUE-'])
        window['-PROGRESS_BAR-'].update(progress_value)

window.close()
    


