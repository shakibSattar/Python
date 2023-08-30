##----Write a program that will give you the in hand salary after deduction of HRA(10%),
# DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),
# (20< _  – 30%)(0-1lakh print k).------

gross_salery = float(input('Enter your gross salary: '))
if gross_salery > 500000 and gross_salery < 1000000:
    tax = (10/100)*gross_salery
    temp_salary = gross_salery - tax
elif gross_salery > 1100000 and gross_salery < 2000000:
    tax = (20/100)* gross_salery
    temp_salary = gross_salery- tax
else:
    tax = (30/100)*gross_salery
    temp_salary = gross_salery - tax
print('after tax reduction, temporary salary is ', temp_salary)


hra = (10/100)* temp_salary
da = (5/100)* temp_salary
pf = (3/100)* temp_salary
in_hand_salary = (temp_salary - hra - da - pf)/12
print('in hand salary is ', in_hand_salary)

if in_hand_salary <=999:
    print(in_hand_salary)
elif in_hand_salary >= 1000 and in_hand_salary <= 99999:
    print(in_hand_salary/1000, 'k')
elif in_hand_salary >= 100000 and in_hand_salary <= 9999999:
    print(in_hand_salary/100000, 'l')
else:
    print(in_hand_salary/10000000, 'cr')
