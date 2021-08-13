import time
print('User and Password Validation!')
print('-----------------------------')

user = input('Type your Username : ')
print('-----------------------------------------------------------')
print("WARNING : Your password can't be the same as your username!")
time.sleep(0.3)
password = input('Type your password :')

while password == user:
    print('Your password needs to be different from your username!')
    print('-----------------------------------------------------------')
    password = input('Type your password : ')
else:
    print('Registration Succeed!')



