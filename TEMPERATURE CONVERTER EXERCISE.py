def celsius():
    print('------------------------\n'
          'Celsius to Fahrenheit !')
    temperature = float(input('Type the Temperature in °C : '))
    F = (temperature * 9 / 5) + 32
    print(f'°F = {F:.2f}\n'
          f'==================')


def fahrenheit():
    print('-------------------------\n'
          'Fahrenheit to celsius !')
    temperature = float(input('Type the Temperature in °F : '))
    C = (temperature - 32) * 5 / 9
    print(f'°C = {C:.2f}\n'
          f'==================')


def choose():
    while True:
        print('Choose the Option!\n'
              '[1] = °C to °F \n[2] = °F to °C')
        choice = int(input('Option : '))

        if choice == 1:
            celsius()
        elif choice == 2:
            fahrenheit()
        else:
            print('ERROR! Remember to Type 1 or 2\n'
                  '-------------------------------')


choose()
