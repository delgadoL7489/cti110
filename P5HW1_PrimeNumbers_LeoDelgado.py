#The prgram tells the user if the inputed number is a prme number or not
#10/1/18
#CTI-110 P5HW1-Prime Numbers
#Leonardo Delgado
#

#Start main function
def main():
#Prompt user to enter the number
    number = int(input('Enter a number: '))
    if is_prime(number):
        print('The number is not prime')
    else:
        print('The number is prime')

#Start callback function
def is_prime(number):
    if (number % 2) == 0:
        status = True
    else:
        status = False
#Return the status of variable
    return status

main()

#Start the main function
#Prompt user for number
#Tests if number meets criteria for prime number
#Outputs response if its prime or not
