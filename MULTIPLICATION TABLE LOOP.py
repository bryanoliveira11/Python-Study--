# Multiplication Table With LOOPS

table = int(input('Multiplication Table Number : '))

for var in range(11):
    results = table * var
    print(table,'x',var,'=',results)