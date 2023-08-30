##----calculates the angles of the hour and minute  while calue of hours and minutes are given---
def calcAngle(H, M):
    if 1<=H<=12 and 0<=M<=59:
        #calculate angle 
        H_angle = (H * 30)+(M * 0.5)
        M_angle = M * 6
        #calculate absulot angle 
        angle = abs(H_angle - M_angle)
        # calculate smaller angle 
        angle = min(360 - angle, angle)
        return print(f'the minimum angle between hour and minute is {angle}')
    else:
        return print('Invalid input. Please enter valid hour (1-12) and minute (0-59).')
    

#call function
hour = int(input('Enter the hour (1-12):'))
minute = int(input('Enter the minute (0-59):'))

angle = calcAngle(hour, minute)
        