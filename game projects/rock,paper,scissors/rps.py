"""
Rock, Paper, Scissors Game

This Python program allows you to play the classic game of Rock, Paper, Scissors against the computer. The objective is to choose your weapon (Rock, Paper, or Scissors) and compete against the computer's randomly selected choice. The program determines the winner based on the game rules and keeps track of the score.

Features:
- Plays a game of Rock, Paper, Scissors against the computer.
- Provides feedback on each player's choice and determines the winner.
- Keeps track of the score and allows you to continue playing or exit the game.
- Supports case-sensitive input for choosing the weapon.

How to Play:
1. Run the program and follow the instructions prompted in the console.
2. Choose your weapon: [R]ock, [P]aper, or [S]cissors.
3. The computer will randomly select its weapon.
4. The program will compare the choices and determine the winner.
5. The game will keep track of the score and display the outcome.
6. Choose to continue playing or exit the game.
7. Play again to challenge the computer to a new game.

Tips:
- Pay attention to the game rules: Rock beats Scissors, Scissors cuts Paper, and Paper covers Rock.
- Strategize your choices based on the computer's tendencies or previous outcomes.
- Aim to improve your score with each playthrough.

Author: [Olajuwon]
Date: [12-05-2022]
"""



import random
import os
import re


def player_status():
    """Return the status of all players."""
    valid_reply= ['Yes','No']
    while True:
        try:
            response=input("Do you want to play current game? (Yes/No)")
            if response not in valid_reply:
                raise ValueError("Yes or No only")
        
            elif response=="Yes":
                return True
            else:
                os.system("cls" if os.name == "nt" else "clear") 
                print("\nThanks for playing!")
                exit()
                
        except ValueError as err:
            print(err)
            
            
def play_rps():
    play=True
    # Define choices and winning combinations
    while play:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Rock, Paper, Scissors - shoot!')
        
        user_option= input('Choose your weapon' '[R]ock, [P]aper, or [S]cissors: ' )
        
        if not re.match("[SsRrPp]", user_option):
            print ('Please choose a letter: ')
            print ('[R]ock, [P]aper, [S]cissors')  
            continue
        
        print (f'You chose: {user_option}')
        
        choices= ['R', 'P', 's']
        comp_choice = random.choice(choices)
        
        print (f"Computer chooses: {comp_choice}")
        
        if comp_choice == user_option.upper() or user_option.lower() :
            print('Tie!')
            play = player_status()
        elif comp_choice == 'R' and user_option.upper() == 'S':
            print ("Rock smash scissors, Computer Wins!")
            play = player_status()
        elif comp_choice == 'S' and user_option.upper() == 'P':
            print ("Scissor cut paper, Computer Win!! ")
            play = player_status()
        elif comp_choice == 'P' and user_option.upper() == 'R':
            print ("Paper covers Rock, Computer Wins!!")
            play = player_status()
        else:
            print('You Win!\n')
            play = player_status()
            

if __name__=='__main__':
    play_rps()                
            
    