##---Write a program that will tell whether the given year is a leap year or not.
year = int(input('Enter a year: '))
if year % 4 == 0:
    print('leap year')
else:
    print('not a leap year')