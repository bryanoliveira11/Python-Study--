import time

print('PYTHON CALCULATOR!')


def addition():
    num1 = float(input('First Number : '))
    num2 = float(input('Second Number : '))
    print(f'Addition = {num1 + num2:.1f}')


def subtraction():
    num1 = float(input('First Number : '))
    num2 = float(input('Second Number : '))
    print(f'Subtraction  = {num1 - num2:.1f}')


def multiplication():
    num1 = float(input('First Number : '))
    num2 = float(input('Second Number : '))
    print(f'Multiplication = {num1 * num2:.1f}')


def division():
    num1 = float(input('First Number : '))
    num2 = float(input('Second Number : '))
    print(f'Division = {num1 / num2:.1f}')


while True:
    print('----------------\n'
          'Select The Math!')
    print('1 - Addiction, 2 - Subtraction, 3 - Multiplication, 4 - Division : ')
    choice = int(input('Math Choice : '))
    print('Wait For It...')
    time.sleep(.5)
    if choice <= 0 or choice > 4:
        print('Please Type a Valid Choice!\n')

    if choice == 1:
        addition()
    elif choice == 2:
        subtraction()
    elif choice == 3:
        multiplication()
    if choice == 4:
        division()
