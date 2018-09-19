#CTI-110
#P3HW2-Shipping Charges
#Leonardo Delgado
#09/18/18
#

#Asks user to input weight of package
weight = int(input('Enter the weight of the package: '))

if weight <= 2:
    print('It is $1.50 per pound')
if 2 < weight <=6:
    print('It is $3.00 per pound')
if 6 < weight <=10:
    print('It is $4.00 per pound')
if weight > 10:
    print('It is $4.75 per pound')

#Prompts user to input weight of package
#Saves value
#Calculates if value is over certain value
#Outputs the specific value for the inputed weight
