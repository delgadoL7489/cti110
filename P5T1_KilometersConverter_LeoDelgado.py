#Prompts user to enter distance in kilmoters and outputs it in miles
#09/30/18
#CTI-110 P5T1_KilometerConverter
#Leonardo Delgado
#

#Get the number to multiply by
Conversion_Factor = 0.6214

#Start the main funtion
def main():
    #Get the distance in kilometers
    kilometers = float(input('Enter a distance in kilometers: '))
    #Display the converted distance.
    show_miles(kilometers)
    
#Start the callback conversion function
def show_miles(km):
    #Formula for conversion 
    miles = km * Conversion_Factor
    #Output converted miles
    print(km, 'kilometers equals', miles, 'miles.')

#Calls back the main funtion
main()


