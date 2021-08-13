def major(x, y, z):
    maj = x

    if y > x:
        maj = y
        if z > y:
            maj = z

    return maj


def minor(x, y, z):
    mini = x

    if y < x:
        mini = y
        if z < y:
            mini = z

    return mini


def number():
    print('### Major And Minor Numbers ###\n'
          '-------------------------------')

    x = int(input('Type the First Number : '))
    y = int(input('Type the Second Number : '))
    z = int(input('Type the Third Number : '))

    print(f'MAJOR = {major(x, y, z)}')
    print(f'MINOR = {minor(x, y, z)}')
    print()


number()
