##---Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

digits = int(input('Enter four digit number: '))
if 1000 <= digits <= 9999:
    digit1 = digits //1000
    digit2 = (digits // 100) % 10
    digit3 = (digits //10) % 10
    digit4 = digits % 10
    reverse = 1000*digit4 +100* digit3 + 10*digit2 + digit1
print('actual number is ', digits)
print('Reversed number is ', reverse)
#check condition
if digits == reverse:
    print('true')
else:
    print('false')
    
    
    
##---OR--- write function to reverse number 
def revered(string):
    return string[::-1]

user_input = (input('Enter four digit number: '))
print(revered(user_input))