#ff
#09/26/18
#CTI-110 P4HW2-Celsius to Fahrenheit Table
#Leonardo Delgado
#

#Print the table heading
print('Celsius\tFahrenheit')
print('-------------------')

#Print celsius temp from 0 to 20
for celsius in range(0, 21):
#Convert celsius to fahrenheit
    fahrenheit = (9/5)*(celsius) + 32
    print(celsius, '\t', fahrenheit)

#Print the table heading
#print a range from 0 to 20
#Convert celsius to fahrenheit
#print the numbers in a table format
