##--Write a program that will take three digits from the user and add the square of each digit.--
number = int(input('Enter thre digits number: '))
if 100<=number<=999:
    number1 = number //100
    number2 = (number //10)%10
    number3 = number%10
    if (number1**3)+(number2**3)+(number3**3) == number:
        print('the number is armstrong')
    else:
        print('number is not arm strong')
else:
    print('Invalid number, try again! ')
    