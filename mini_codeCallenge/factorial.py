##-------Write a program that can find the factorial of a given number
# provided by the user.--------
number = int(input('Enter a number: '))
i = 1
if number > 0:
    while number >= 1:
        i = i * number
        number = number - 1
    print('factorial of a given number is: ', i)
else:
    print('factorial of given number is not possible.')
    