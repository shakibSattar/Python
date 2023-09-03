##--Write a program that will tell whether the number entered by the user is odd or even.
number = int(input('Enter number: '))
if number %2 == 0:
    print('even')
else:
    print('odd')
    
    
    
    
##-----Write a program to print the first 25 odd numbers----
intager = 0
number = 1
while True:
    if number % 2 != 0:
        print(number)
        intager += 1
    if intager == 25:
        break
    
    number += 1
        

