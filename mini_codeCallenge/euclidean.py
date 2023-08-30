##---Write a program to find the euclidean distance between two coordinates.----
x1 = int(input('Enter x1 for x coordinate: '))
y1 = int(input('Enter y1 for y coordinate: '))
x2 = int(input('Enter x2 for x coordinate: '))
y2 = int(input('Enter y2 for y coordinate: '))

z = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(z)
