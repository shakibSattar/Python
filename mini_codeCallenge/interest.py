##---Write a program to find the simple interest when the value of principle,
# rate of interest and time period is given.-----

principal = float(input('Enter principal amount: '))
rate = float(input('Enter interest rate: '))
time = int(input('Enter time period: '))

interest = (principal * rate * time)/100
print(f'the simple interest amount is {interest}')

amount = principal + interest
print(f'your total  rmainig amount is {amount}')
