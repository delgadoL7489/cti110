#Tells the user the total amount of bugs thats been caught throughout the week
#09/20/18
#CTI-110 P4T2-Bug Collector
#Leonardo Delgado
#

#Initialize the accumulator
total = 0

#Get the bugs collected for each day
for day in range(1, 8):
    #Prompt user for amount of bugs that day
    print('Enter the bugs collected on day', day)
    #User must input number of bugs
    bugs = int(input())
    #Gets the total for the week
    total = total + bugs

#Display the total bugs
print('You collected a total of', total, 'bugs.')
