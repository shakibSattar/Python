##---Write a program that will determine weather when the value of 
# temperature and humidity is provided by the user.
#TEMPERATURE(C)      HUMIDITY(%)      WEATHER

#      >= 30                             >=90                 Hot and Humid
#      >= 30                             < 90                 Hot
#      <30                               >= 90                Cool and Humid
#      <30                                <90                 Cool

temprature = int(input('Enter temprature: '))
humidity = int(input('Enter humidity: '))
if temprature >= 30 and humidity >= 90:
    print('the weather is hot and humid ')
elif temprature >= 30 and humidity < 90:
    print('the weather is hot')
elif temprature < 30 and humidity >= 90:
    print('the weather is cool and humid')
else:
    print('the weather is cool')

    