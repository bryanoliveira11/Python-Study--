import time

product = 1
count = 1
price = total_price = pay = 0


print('Remember to Type 0 to end your shopping!')
while product != 0:
    print('------------------------------------')
    time.sleep(0.1)
    price = float(input(f'Type the product price {count} :  $'))
    count += 1
    total_price += price
    if price == 0:
        print('------------------------------------')
        print(f'Total price = {total_price:.2f} $')
        pay = float(input('Money to pay =  $'))
        print(f'Change = {pay - total_price:.2f} $')
        if total_price > pay:
            print("Seems like you don't have enough money! GET OUT!")
        total_price = 0
        count = 1



