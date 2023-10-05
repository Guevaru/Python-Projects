"""
Dice Rolling Game

This Python program allows you to roll one or two dice and observe the outcome. You can choose the number of dice you want to roll, and the program will generate random values for each dice. After rolling the dice, the program displays the values and calculates the total, if applicable. You can choose to roll the dice again or exit the game.

Features:
- Rolls one or two dice based on user input.
- Generates random values for each dice.
- Calculates and displays the total value for two dice rolls.
- Allows the user to roll the dice again or exit the game.

How to Play:
1. Run the program and follow the instructions prompted in the console.
2. Enter the number of dice you want to roll: '1' or '2'.
3. The program will generate random values for each dice.
4. If you chose to roll two dice, the program will calculate and display the total value.
5. The program will show the values and the total (if applicable).
6. Choose to roll the dice again or exit the game.
7. Roll again to observe different outcomes.

Tips:
- Experiment with different numbers of dice to observe various results.
- Keep track of the values and totals to analyze the distribution of outcomes.
- Have fun exploring the randomness of dice rolls!

Author: [Olajuwon]
Date: [29-05-2022]
"""



import random
import os



def die_num():
    while True:
        try:
            num_dice= input('Number of dice: ')
            valid_reply=['1','one','2','two']
            if num_dice not in valid_reply:
                raise ValueError('1 or 2 only')
            else:
                return (num_dice)
            
        except ValueError as err:
            print(err)
            
            
def dice_roll():
    min_val=1
    max_val=6
    roll_again= 'y' or 'yes'
    
    while roll_again.lower() == 'y' or roll_again.lower() == 'yes': 
        os.system('cls' if os.name == 'nt' else 'clear')
        amount = die_num()
        
        if amount == '2' or amount == 'two' :
            print ('Rolling sthunderrr......')
            dice_1 = random.randint(min_val,max_val)
            dice_2 = random.randint(min_val,max_val)
            total= dice_1 + dice_2
                
            print('The values are: ')
            print(f'Dice one: {dice_1}')
            print(f'Dice Two:  {dice_2}')
            print(f'Total : {dice_1} + {dice_2} = {total} ' )
        
            roll_again = input('Roll Again?  ')
        else:
            print(f'Rolling the die...')
            dice_1 = random.randint(min_val, max_val)
            print(f'The Value is: {dice_1}')
            
            roll_again = input('Roll Again? ')
            
            
if __name__ == '__main__':
    dice_roll()
            
            
                  

                   