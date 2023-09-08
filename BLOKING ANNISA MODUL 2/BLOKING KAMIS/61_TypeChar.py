import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [[sg.Text('Your typed char appear here:'), sg.Text(size=(15,1), key='_OUTPUT_')], 
          [sg.Input(key='_IN_')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Pattern 28', layout)

while True: 
    event, values= window.read()
    print(event, values)
    if event == 'Show':

        window['_OUTPUT_'].update(values['_IN_'])

    window.close()