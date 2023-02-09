import PySimpleGUI as sg
import random
sg.change_look_and_feel('DarkBlue')
error_msg_color = ['#fa4437','#42a1ff','#fff53b']

ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSOR = 'SCISSOR'

choices = {
    ROCK: 'ROCK',
    PAPER: 'PAPER',
    SCISSOR: 'SCISSOR'
}

win_lose_draw = {
(ROCK, SCISSOR): 'WIN',
(PAPER, ROCK): 'WIN',
(SCISSOR, PAPER): 'WIN',
(ROCK, PAPER): 'LOSE',
(PAPER, SCISSOR): 'LOSE',
(SCISSOR, ROCK): 'LOSE',
(ROCK, ROCK): 'DRAW',
(PAPER, PAPER): 'DRAW',
(SCISSOR, SCISSOR): 'DRAW',
}

def start_screen():
    global start_screen_layout,game_number_validation,win_count

    win_count = []

    game_title_text = [sg.Text('   '),sg.Text('ROCK',font=('Cooper Black',15)),sg.Text('PAPER',font=('Cooper Black',15),pad=(55,0)),sg.Text('SCISSORS',font=('Cooper Black',15)),],
    game_imgs = [sg.Image(r'C:\Users\bryan.oliveira\Desktop\Python\rock_paper_scissor_PROJECT\img\rock_bg.png',key='-rock-'),sg.Image(r'C:\Users\bryan.oliveira\Desktop\Python\rock_paper_scissor_PROJECT\img\paper_bg.png',key='-paper-'),sg.Image(r'C:\Users\bryan.oliveira\Desktop\Python\rock_paper_scissor_PROJECT\img\scissors_bg.png',key='-scissors-')],
    game_number_text = [sg.Text(' '),sg.Text('Number of Games :',font=('Cooper Black',18))],
    game_input_battleNum = [sg.Text(''),sg.Input(key='battle_number',size=(6),font=('Arial',20))],
    game_start_button = [sg.Text(' '),sg.Button('-START-',font='Arial')],
    game_error_return = [[sg.Text(' '),sg.Text('',key='error_msg',font=('Arial',16))]]

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

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == '-START-':
            start_screen_layout['error_msg'].update(text_color=random.choice(error_msg_color))
            game_number_validation = (values['battle_number'])
            
            try :
                if game_number_validation == '' or int(game_number_validation) <= 0:
                    start_screen_layout['error_msg'].update('[INFO] : Input Must be a Number > 0 !')
                else:
                    start_screen_layout.close()
                    return start_game()
            except ValueError as ve:
                start_screen_layout['error_msg'].update(f'[INFO] : {ve}')

def start_game():
    global player_weapon_choice,battle_count

    battle_count = 1
    player_weapon_choice = 'ROCK'

    game_title_battle = [sg.Text(f'Battle {battle_count}',font=('Cooper Black',20),key='game_title_battle')],
    game_choose_weapon = [sg.Text(f' Choose Your Weapon : ',font=('Arial',18))],
    game_img_choice = [sg.Image(r'C:\Users\bryan.oliveira\Desktop\Python\rock_paper_scissor_PROJECT\img\rock_bg.png',key='-rock-'),sg.Image(r'C:\Users\bryan.oliveira\Desktop\Python\rock_paper_scissor_PROJECT\img\paper_bg.png',key='-paper-'),sg.Image(r'C:\Users\bryan.oliveira\Desktop\Python\rock_paper_scissor_PROJECT\img\scissors_bg.png',key='-scissors-')],
    game_checkboxes = [sg.Checkbox('ROCK',default=False,enable_events=True,key='-choice_rock-',),sg.Text('',size=(7,1)),sg.Checkbox(' PAPER',default=False,enable_events=True,key='-choice_paper-'),sg.Text('',size=(6,1)),sg.Checkbox(' SCISSORS',default=False,enable_events=True,key='-choice_scissors-')],
    game_start_button = [sg.Text(' '),sg.Button('-BATTLE-',font='Arial')],
    game_error_return = [[sg.Text(' '),sg.Text('',key='error_msg',font=('Arial',16))]]

    layout_geral = [
        [sg.Column(game_title_battle,justification='center',element_justification='center')],
        [sg.Column(game_choose_weapon,justification='center',element_justification='center')],
        [sg.Column(game_img_choice,justification='center',element_justification='center')],
        [sg.Column(game_checkboxes,justification='center',element_justification='center')],
        [sg.Column(game_start_button,justification='center',element_justification='center')],
        [sg.Column(game_error_return,justification='center',element_justification='center')]]

    game_screen_layout = sg.Window('GAME',size=(600,375),finalize=True,layout=layout_geral)

    while True:
        event, values = game_screen_layout.read()

        if event == '-choice_rock-':
            game_screen_layout['-choice_paper-'].update(False)
            game_screen_layout['-choice_scissors-'].update(False)
            player_weapon_choice = 'ROCK'

        elif event == '-choice_paper-':
            game_screen_layout['-choice_rock-'].update(False)
            game_screen_layout['-choice_scissors-'].update(False)
            player_weapon_choice = 'PAPER'

        elif event == '-choice_scissors-':
            game_screen_layout['-choice_paper-'].update(False)
            game_screen_layout['-choice_rock-'].update(False)
            player_weapon_choice = 'SCISSOR'

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == '-BATTLE-':
            game_screen_layout['error_msg'].update(text_color=random.choice(error_msg_color))

            if battle_count <= int(game_number_validation):
                if battle_count == int(game_number_validation) + 1:
                    game_screen_layout['error_msg'].update('Battle Ended !')

                elif values['-choice_rock-'] == False and values['-choice_paper-'] == False and values['-choice_scissors-'] == False:
                    game_screen_layout['error_msg'].update('[INFO] : Check Only One Checkbox !')
                else:
                    battle_count += 1
                    game_screen_layout['game_title_battle'].update(f'Battle {battle_count}')
                    game_screen_layout.close()
                    return battle_screen()

            game_screen_layout['-choice_rock-'].update(False)
            game_screen_layout['-choice_paper-'].update(False)
            game_screen_layout['-choice_scissors-'].update(False)
    

def enemy_battle_choice():
    return random.choice(list(choices.keys()))

def battle_screen():

    game_battle_count = [sg.Text(f'Battle {battle_count}',font=('Cooper Black',20),key='game_title_battle')],
    game_battle_imgs = [sg.Image(r'C:\Users\bryan.oliveira\Desktop\Python\rock_paper_scissor_PROJECT\img\rock_bg.png',key='-rock-'),sg.Text('',size=(14,1)),sg.Image(r'C:\Users\bryan.oliveira\Desktop\Python\rock_paper_scissor_PROJECT\img\scissors_bg.png',key='-scissors-')],
    game_battle_choices = [sg.Text('',key='-player-',font=('Cooper Black',15)),sg.Text("",size=(20,1)),sg.Text('',key='-enemy-',font=('Cooper Black',15))],
    game_battle_next = [sg.Text(' '),sg.Button('-NEXT-',font='Arial')],

    layout_geral = [
        [sg.Column(game_battle_count,justification='center',element_justification='center')],
        [sg.Column(game_battle_imgs,justification='center',element_justification='center')],
        [sg.Column(game_battle_choices,justification='center',element_justification='center')],
        [sg.Column(game_battle_next,justification='center',element_justification='center')],]

    battle_screen_layout = sg.Window('GAME',size=(600,375),finalize=True,layout=layout_geral)

    enemy_b_choice = enemy_battle_choice()
    battle_screen_layout['-player-'].update(player_weapon_choice)
    battle_screen_layout['-enemy-'].update(enemy_b_choice)

    while True:
        event, values = battle_screen_layout.read()

        if event == sg.WIN_CLOSED or event== "Exit" :
                break
        elif event == '-NEXT-':
            result = win_lose_draw.get((player_weapon_choice, enemy_b_choice))

if __name__ == '__main__':
    start_screen()
