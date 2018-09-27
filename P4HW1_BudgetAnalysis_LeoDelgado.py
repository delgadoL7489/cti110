#Program prompts user for budget and tells if user is over or under budget 
#09/23/18
#CTI-110 P4HW1-Budget Analysis
#Leonardo Delgado
#

#Prompt user for budget
budget = int(input('Enter the budget for the month: '))
keep_going = 'y'
total = 0

#prompts the user for the expenses for the month
while keep_going == 'y':
    expenses = int(input('Enter expense: '))
#Calculate total 
    total = total + expenses
    under = budget - total
    over = budget + total
#Asks for anymore expenses 
    keep_going = input('Any more expenses?(Enter y/n): ')

#Outputs your total and if youre under or over budget
if budget >= total:
    print('Your total is $',total,'Youre under budget by: $',under)
if budget < total:
    print('Your total is $',total,'Youre over budget by:$', over)

#Prompt the user for a budget
#Prompots for expenses
#Calculate total
#Outputs total and if youre over or under budget
