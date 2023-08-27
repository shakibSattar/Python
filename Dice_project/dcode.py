import Dice

while True:
    user  = int(input("Enter number of Dice: "))
    if user == 0:
        break
    Dice.findDice(user)
    