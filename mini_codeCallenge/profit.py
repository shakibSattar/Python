##-------Write a program that will take user input of cost price and selling 
# price and determines whether its a loss or a profit -------

cost = int(input('Enter cost price: '))
sell = int(input('Enter selling price: '))
if cost < sell:
    amount = sell - cost
    print(f'there is profit of {amount}')
else:
    amount = cost - sell
    print(f'there is lost of {amount}')