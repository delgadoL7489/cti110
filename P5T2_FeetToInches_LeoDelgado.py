#Make a code to convert a number of feets to inches
#09/30/18
#CTI-110 P5T2_FeetToInches
#Leonardo Delgado
#

#Set a value
Inches_Per_Foot = 12

#Main function
def main():
    #Prompts user for number of feet
    feet = int(input('Enter a number of feet: '))
    #Convert to inches
    print(feet, 'equals', feet_to_inches(feet), 'inches.')                 

#Formula for conversions
def feet_to_inches(feet):
    return feet * Inches_Per_Foot

#Call the main function
main()

#Prompt user for the number of feet
#convert feet to inches
#output the converted number
