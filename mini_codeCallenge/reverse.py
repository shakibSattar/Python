##---Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

user = int(input('Enter four digit number: '))
number = user

a = number %10
number = number // 10

b = number % 10
number = number // 10

c = number % 10
d = number //  10

#apply forumla to reverse four digit number 
reverse = 1000*a + 100*b + 10*c + d
print('actual number is ', user)
print('Reversed number is ', reverse)
#check condition
if user == reverse:
    print('true')
else:
    print('false')
    
    
    
##---OR--- write function to reverse number 
def revered(string):
    return string[::-1]

user_input = (input('Enter four digit number: '))
print(revered(user_input))