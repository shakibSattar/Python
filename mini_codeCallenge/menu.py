##----Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit-----
user_choice = (input('''Welcome to my page,
                   what would you like to do fromthe following menu: '))
                   1. covert cm to ft
                   2. convert kl to miles
                   3. convert $ dollor to ruppiess
                   4. Exit 
                   please enter your choice: '''))

if user_choice == '1':
    cm = float(input('Enter value in cm: '))
    feet = cm/30.48
    print(f'the value {cm} coverted in fee is {feet}')
elif user_choice == '2': 
    kl = float(input('Enter the value in kl: '))
    miles = kl * 0.621
    print(f'the value of {kl} is converted in miles is {miles}')
elif user_choice == '3':
    dollor = float(input('Enter amount in US dollor: '))
    pk_ruppies = dollor * 304.70
    print(f'{dollor} US dollor is converted to {pk_ruppies} pakistani ruppies')
else:
    print('Exit')
    
    
