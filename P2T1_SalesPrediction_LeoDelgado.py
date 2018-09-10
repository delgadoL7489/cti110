# Get the projected total sales
#09/09/18
#CTI-110 P2T1-Sales Prediction
#Leonardo Delgado
#
#Get the projected total sales
total_sales = float(input('Enter the projected sales: '))

#Calculate the profit as 23 percent of toal sales
profit = total_sales * 0.23

#Display the profit
print('The profit is $', format(profit, ',.2f'))
