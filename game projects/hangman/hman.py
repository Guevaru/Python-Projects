"""
Hangman Game

This Python program allows you to play the classic game of Hangman. The objective is to guess a hidden word by guessing individual letters. With each incorrect guess, a part of the hangman is drawn. The game continues until you guess the word correctly or the hangman is completed.

Features:
- Prompts the player to enter their name and welcomes them to the game.
- Retrieves a random word from a file to use as the hangman word.
- Allows the player to guess individual letters to reveal the word.
- Keeps track of incorrect guesses and draws the hangman accordingly.
- Provides feedback on correct and incorrect guesses.
- Allows the player to play multiple games and provides an option to play again.

How to Play:
1. Run the program and follow the instructions prompted in the console.
2. Enter your name when prompted.
3. The program will generate a random word from the word bank.
4. Guess individual letters to reveal the word.
5. If your guess is correct, the corresponding letter(s) will be displayed.
6. If your guess is incorrect, the hangman will be drawn, and the number of remaining guesses will be shown.
7. Keep guessing until you correctly guess the word or the hangman is completed.
8. After each game, choose to play again or exit the game.

Tips:
- Pay attention to the remaining guesses and adjust your strategy accordingly.
- Try to guess common letters first to reveal more of the word.
- Consider the partially revealed word to make educated guesses.
- Keep track of your progress to avoid repeating incorrect guesses.

Author: [Olajuwon]
Date: [20-09-2022]
"""



import random
import time
import os


def play_again():
    question = 'Do you want to play again? (y = yes, n = no) \n'
    play_game = input(question)
    while play_game.lower() not in ['y', 'n']:
        play_game = input(question)

    if play_game.lower() == 'y':
        return True
    else:
        return False



def fetch_word():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'words.txt')
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return random.choice(words)



def hangman(word):
    display = '_' * len(word)
    count = 0
    limit = 5
    letters = list(word)
    guessed = []
    while count < limit:
        guess = input(f'Hangman Word: {display} Enter your guess: \n').strip()
        while len(guess) == 0 or len(guess) > 1:
            print('Invalid input. Enter a single letter\n')
            guess = input(
                f'Hangman Word: {display} Enter your guess: \n').strip()

        if guess in guessed:
            print('Oops! You already tried that guess, try again!\n')
            continue

        if guess in letters:
            letters.remove(guess)
            indices = [i for i, x in enumerate(word) if x == guess]
            for index in indices:
                display = display[:index] + guess + display[index + 1:]

        else:
            guessed.append(guess)
            count += 1
            draw_hangman(count, limit)
            print(f'Wrong guess: {limit - count} guesses remaining\n')

        if display == word:
            print(f'Congrats! You have guessed the word \'{word}\' correctly!')
            break


def draw_hangman(count, limit):
    stages = [
        """
           _____ 
          |      
          |      
          |      
          |      
          |      
          |      
        __|__
        """,
        """
           _____ 
          |     | 
          |     | 
          |      
          |      
          |      
          |      
        __|__
        """,
        """
           _____ 
          |     | 
          |     | 
          |     | 
          |      
          |      
          |      
        __|__
        """,
        """
           _____ 
          |     | 
          |     | 
          |     | 
          |     O 
          |      
          |      
        __|__
        """,
        """
           _____ 
          |     | 
          |     | 
          |     | 
          |     O 
          |    /|\ 
          |    / \ 
        __|__
        """
    ]
    if count >= 0 and count < len(stages):
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(stages[count])
    else:
        print('you are already dead.')



def play_hangman():
    print('\nWelcome to Hangman\n')
    name = input('Enter your name: ')
    print(f'Hello {name}! Best of Luck!')
    time.sleep(1)
    print('The game is about to start!\nLet\'s play Hangman!')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    play = True
    while play:
        word = fetch_word()
        hangman(word)
        play = play_again()

    print('Thanks for playing! We hope to see you again!')
    exit()


if __name__ == '__main__':
    play_hangman()


