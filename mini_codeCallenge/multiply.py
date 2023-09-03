##--------Write a program that can multiply 2 numbers provided by the user 
# without using the * operator--------
first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
multiple = 0
for n in range(0,first_num):
    multiple += second_num
print(' the result of multiplacation of the value is ',multiple)
    
    
