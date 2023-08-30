##--Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.--
A = int(input('Enter angle 1:'))
B = int(input('Enter angle 2:'))
C = int(input('Enter angle 3:'))

if A+B+C ==180 and A!=0 and B !=0 and C !=0:
    print('triangle is Possible')
else:
    print('triangle is not possible')
    