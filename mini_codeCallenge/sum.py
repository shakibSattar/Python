# ##---Write a program that will give you the sum of 3 digits---
num1 = 32
num2 = 22
num3 = 55
total_sum  = num1 + num2 + num3
print(total_sum)


##-----OR--- sum number given by user 
number1 = int(input('Enter number1: '))
number2 = int(input('Enter number2: '))
number3 = int(input('Enter number3: '))

numbers = [number1, number2, number3]
total = sum(numbers)
print(total)

##--- Add thre numbers that given one  user 
number = int(input('Enter number: '))

a =  number % 10     #(345 % 10 = 5)
number = number // 10 #(345 // 10 = 34)
b = number % 10  #(34 % 10 = 4)
c = number // 10 #(34 // 10 = 3)
sum_num = a+b+c
print(sum_num)



