import PySimpleGUI as sg
import random

def start_screen():
    global start_screen_layout
    sg.change_look_and_feel('DarkBlue')

    game_title_text = [sg.Text('   '),sg.Text('ROCK',font=('Cooper Black',15)),sg.Text('PAPER',font=('Cooper Black',15),pad=(55,0)),sg.Text('SCISSORS',font=('Cooper Black',15)),],
    game_imgs = [sg.Image(r'C:\Users\bryan.oliveira\Desktop\Python\rock_paper_scissor_PROJECT\img\rock_bg.png'),sg.Image(r'C:\Users\bryan.oliveira\Desktop\Python\rock_paper_scissor_PROJECT\img\paper_bg.png'),sg.Image(r'C:\Users\bryan.oliveira\Desktop\Python\rock_paper_scissor_PROJECT\img\scissors_bg.png')],
    game_number_text = [sg.Text(' '),sg.Text('Number of Games :',font=('Cooper Black',18))],
    game_input_battleNum = [sg.Text(''),sg.Input(key='battle_number',size=(6),font=('Arial',20))],
    game_start_button = [sg.Text(' '),sg.Button('-START-',font='Arial')],
    game_error_return = [[sg.Text(' '),sg.Text('',key='error_msg',font='Arial')]]

    layout_geral = [
        [sg.Column(game_title_text,justification='center',element_justification='center')],
        [sg.Column(game_imgs,justification='center',element_justification='center')],
        [sg.Column(game_number_text,justification='center',element_justification='center')],
        [sg.Column(game_input_battleNum,justification='center',element_justification='center')],
        [sg.Column(game_start_button,justification='center',element_justification='center')],
        [sg.Column(game_error_return,justification='center',element_justification='center')]]
    
    start_screen_layout = sg.Window('START',size=(600,375),finalize=True,layout=layout_geral)

    while True:
        event, values = start_screen_layout.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == '-START-':
            game_number_validation = values['battle_number']

            try :
                if game_number_validation <= 0 or game_number_validation == '':
                    start_screen_layout.find_element('battle_number').update('')
                    start_screen_layout['error_msg'].update('[INFO] : Input Must be a Number > 0 !')
                else:
                    start_game()
            except ValueError as ve:
                start_screen['error_msg'].update(f'[INFO] : {ve}')
                #start_screen.hide()
                return start_screen()

def start_game():
    pass

if __name__ == '__main__':
    start_screen()