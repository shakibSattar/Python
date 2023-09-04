##-----Write a program to print whether a given number is prime number or not-----

n = int(input('Enter a number: '))
if n ==2:
    print('number is prime number: ')
elif n>1:
    for i in range(2, n):
        if(n % i) == 0:
            print(f'{n} is not a prime number')
            break
        else:
            print(f'{n} is a prime number')
            break
    else:
        print(f'{n} is not a prime number')
        
