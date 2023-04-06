import random

ROCK = 1
PAPER = 2
SCISSOR = 3

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

def start_game():
    global number_of_rounds, win_count
    try:
        number_of_rounds = int(input('\nInput the Number of Matches: '))
        if number_of_rounds <= 0:
            raise ValueError('Number of rounds must be greater than 0')
    except ValueError as ve:
        print(f'\n[ERROR] {ve}')
        return start_game()

    win_count = []

    for i in range(1, number_of_rounds + 1):
        print(f'\n -- Round Number {i} -- ')
        result = battle_result()
        print(result)

def player_choice():
    try:
        choice = int(input('\nInput Your Choice:\n''1 - ROCK\n''2 - PAPER\n''3 - SCISSOR\n'': '))
        if choice not in choices:
            raise ValueError('Input must be 1, 2 or 3')
        return choice
    except ValueError as ve:
        print(f'\n[ERROR] {ve}')
        return player_choice()

def auto_choice_enemy():
    return random.choice(list(choices.keys()))

def battle_result():
    player = player_choice()
    enemy = auto_choice_enemy()
    result = win_lose_draw.get((player, enemy))

    print(f'\n Your Choice = {choices[player]}   VS   Enemy Choice = {choices[enemy]}')

    if result == 'WIN':
        win_count.append(1)
        return '\n\t\tYou Won !'
    elif result == 'LOSE':
        return '\n\t\tYou Lost !'
    else:
        return '\n\t\tDraw !'

if __name__ == '__main__':
    start_game()
    print(f"\n     You Have Won {len(win_count)} from {number_of_rounds} Rounds !")
