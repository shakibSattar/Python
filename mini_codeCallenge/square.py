##---Write a program that will take three digits from the user and add the square of each digit.---
digits = int(input('Enter a three digir number: '))

if 100 <= digits <= 999:
    digit1 = digits //100
    digit2 = (digits // 10) % 10
    digit3 = digits  % 10
  
    reverse = digit1**2 + digit2**2 + digit3**2
    print(reverse)
else:
    print('invalid number')
    
