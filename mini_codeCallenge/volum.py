##--Write a program to find the volume of the cylinder. Also find the cost when 
# when the cost of 1litre milk is 40Rs.------


radius = float(input('Enter radius: '))
height = float(input('Enter height: '))
#formula to find volum
volum = 3.14*(radius)**2 * height
#formula to find cost
cost = (volum/1000)* 40 # 40 is price per litre
print(f'Volume of cylinder is {volum} and the cost is {cost}')