##---Write a program that will tell the number of dogs and chicken are there
# when the user will provide the value of total heads and legs.----

head = int(input('Enter number of heads: '))
legs = int(input('Enter number of legs: '))
for chicken in range(head +1):
    dog = head - chicken
    if (2*chicken)+(4*dog) == legs:
        print(f'number of chicken is {chicken}')   
        print(f'number of dogs are {dog}')
        break
    else:
        print("Cannot determine the number of chickens and dogs with given input.")


