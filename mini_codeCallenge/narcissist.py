##--Write a program that will take user input of (4 digits number) and check whether the number is
# narcissist number or not.--
number = int(input('Enter four digits number: '))
if 1000<=number<=9999:
    number1 = number // 1000
    number2 = (number //100)%10
    number3 = (number//10)%10
    number4 = number%10
    if(number1**4)+(number2**4)+(number3**4)+ (number4**4) == number:
        print('number is narcissist')
    else:
        print('number is not narcissist')
else:
    print('number is Invalid, Try again!')
    