print('----------------------------------------------------------------\n'
      '''                      COUNTING NUMBERS!''')
print('----------------------------------------------------------------')
print('TIPS : \n'
      'Type a Negative Number to Stop!\n'
      '')

n = 1
numb1 = numb2 = numb3 = numb4 = 0

while n > 0:
    n = int(input('Type Aleatory Numbers Between 0 And 100 : '))
    if (n >= 0) and (n <= 25):
        numb1 += 1
    elif (n >= 26) and (n <= 50):
        numb2 += 1
    elif (n >= 51) and (n <= 75):
        numb3 += 1
    elif (n >= 76) and (n <= 100):
        numb4 += 1
        if n < 0:
            break

print(f'Numbers Between 0 and 25: {numb1} \n'
      f'Numbers Between 26 and 50: {numb2} \n'
      f'Numbers Between 51 and 75: {numb3} \n'
      f'Numbers Between 76 and 100: {numb4} \n')
