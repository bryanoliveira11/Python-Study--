import pyautogui
import time

def autoStart():
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    time.sleep(.3)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(.3)

def startMission():
    print('\n - Começando Missão')
    autoStart()
    autoStart()
    autoStart()
    autoStart()
    autoBattle()

def battleKeyboard():
    time.sleep(1)
    pyautogui.keyDown('e')
    pyautogui.keyDown('i')
    pyautogui.keyUp('i')
    time.sleep(2)
    pyautogui.keyDown('i')
    pyautogui.keyUp('i')
    pyautogui.keyUp('e')
    pyautogui.keyDown('f')
    pyautogui.keyDown('i')
    pyautogui.keyUp('i')
    pyautogui.keyUp('f')

def autoBattle():
    time.sleep(6.2)
    count = 0
    while count != 6:
        battleKeyboard()
        count += 1
        print(f' - Executou Função battleKeyboard() {count} Vezes')
        if count == 6:
            pyautogui.keyDown('esc')
            pyautogui.keyUp('esc')
            time.sleep(15.5)
            startMission()

def startApp():
    try:
        start = str(input('\nComeçar ? \n\n''Y - Sim ; N - Não\n\n''= '))
        start.lower()
        if start == 'y':
            print('\nAbra o Jogo !')
            i = 5
            while i >= 0:
                time.sleep(1)
                print(f' - Começando em {i} !')
                i -= 1
            startMission()
        else: 
            print("\n - ok")
            startApp()
    except:
        startApp()

startApp()
