#The program lets the user play Rock,Paper, Scissors
#10/1/18
#CTI-110 P5HW2-Rock,Paper,Scissors Game
#Leonardo Delgado
#

#import the random tool
import random

#assign the computers choices
comp_choice = random.randint(1, 3)
#Prompt user for their choice
choice = input('Choose either rock, paper, or scissors?: ')

#Start main function
def main():
    #Options if user chose rock
    if choice == 'rock':
        if comp_choice == 2:
            print('Computer chose paper You lose!')
        elif comp_choice == 3:
            print('Computer chose scissors You win!')
        else:
            print('Tie')
    #Options if user chose paper        
    elif choice == 'paper':
        if comp_choice == 1:
            print('Computer chose rock You win!')
        elif comp_choice == 3:
            print('Computer chose scissors You lose!')
        else:
            print('Tie')
    #Options if user chose scissors
    elif choice == 'scissors':
        if comp_choice == 1:
            print('Computer chose rock You lose!')
        elif comp_choice == 2:
            print('Computer chose paper You win!')
        else:
            print('Tie')
       
main()

#Prompt user for choice
#If Rock output is you win, lose or tie
#If Paper output is you win, lose or tie
#If Scissors output is you win, lose or tie

