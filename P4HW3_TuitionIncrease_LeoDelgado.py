#I have to find the increased tution of a school for the next 5 years
#09/26/18
#CTI-110 P4HW3-Tuition Increase
#Leonardo Delgado
#

#Setting up the loop
tuition = 8000
keep_going = 'y'

#Beginning the loop
while keep_going == 'y':
#Prompt for the specific year
    year = int(input('What year between 1-5: '))
#Calculate the tuition for the specified year
    new_tuition = tuition*(1.03**year)
#Outputs the tuition cost for that year
    print('Your tuition for year', year,'will be $', format(new_tuition,',.2f'))
#Asks for another year
    keep_going = input('Enter another year?(Enter y/n): ')

#Set up loop conditions
#Begin the loop
#Prompt user to input specified year
#Calculate tuition
#Outputs the tuition for the inputted year
