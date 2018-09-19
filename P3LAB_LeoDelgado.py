# I took a bugged and partially done code and finished it.
# CTI-110
# P3LAB- Debugging
# Leonardo Delgado
# 09/17/18

def main():
  print("Welcome to Grade Converter!")
  
# program start
print('Welcome to Grade Conerter!')
print("Here we will take a number grade and change it to a letter grade!")
print('--------------------------------------------------------------------')

# This program takes a number grade and outputs a letter grade.
# system uses 10-point grading scale

# Get test score from the user
# Use float for number grades that use decimals
score = float(input('Enter grade: '))

# Define the rest of the scores
A_score = 90
B_score = 80
C_score = 70
D_score = 60

#Determine the grade
if score >= A_score:
    print('Your grade is: A') 
elif score >= B_score:
    print('Your grade is: B')
elif score >= C_score:
    print('Your grade is: C')
elif score >= D_score:
    print('Your grade is: D')
else: 
    print('Your grade is: F')
