"""
Guess the Name Game

This Python program is a word guessing game where the player attempts to guess a random name chosen from a list of names. The game provides hints and tracks the player's attempts and high score.

Features:
- Randomly selects a name from a file to guess.
- Provides hints, including random letters from the name, number of vowels, consonants, and the first letter.
- Keeps track of the player's attempts and displays the high score.
- Allows the player to continue playing or exit the game.

How to Play:
1. Run the program and follow the instructions prompted in the console.
2. Enter 'yes' if you want to play the game.
3. The program will select a random name for you to guess.
4. It will provide hints to assist your guessing process.
5. Enter your guess for the name.
6. If your guess is incorrect, the program will inform you and prompt for another guess.
7. The game will continue until you guess the correct name.
8. After each round, choose to play again or exit the game.

Tips:
- Pay attention to the hints provided to narrow down your guesses.
- Be mindful of the number of attempts to try to beat your high score.
- Aim to improve your guessing skills with each playthrough.

Author: [Olajuwon]
Date: [15-09-2022]
"""


import random
import os

def get_words():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'name.txt')
    with open(file_path, 'r') as file:
        words = [word.strip() for word in file.readlines()]
    return words

def show_hint():
    words = get_words()
    word = random.choice(words)
    length = len(word)

    position1 = random.randint(1, length)
    position2 = random.randint(1, length)
    while position2 == position1:
        position2 = random.randint(1, length)

    hint_letter1 = word[position1 - 1]
    hint_letter2 = word[position2 - 1]

    vowels = ['A', 'E', 'I', 'O', 'U']
    num_vowels = sum(1 for letter in word if letter.upper() in vowels)
    num_consonants = length - num_vowels

    first_letter = word[0]

    random_letters = random.sample(word, 3)

    hint = f'Here is a random letter from the name: "{hint_letter1}" at position {position1}, and another letter: "{hint_letter2}" at position {position2}.'
    hint += f'\nThe length of the word is {length}.'
    hint += f'\nNumber of vowels: {num_vowels}'
    hint += f'\nNumber of consonants: {num_consonants}'
    hint += f'\nThe first letter of the word is: {first_letter}.'
    hint += f'\nAdditional random letters: {" ".join(random_letters)}.'
    return hint

def begin_game():
    player_attempts = []

    print('Hello there, let\'s make guesses together')
    wanna_play = input('Enter yes if you want to play: ')

    if wanna_play.lower() != 'yes':
        print('Please enter correct input')
        exit()
    else:
        words = get_words()
        print(show_hint())

    while wanna_play.lower() == 'yes':
        try:
            guess_word = input("Guess the Name: ")
            if not guess_word or not guess_word[0].isupper() or not guess_word.isalpha():
                raise ValueError('Enter a proper name starting with a capital letter')

            attempts = 1

            while guess_word.lower() not in [word.lower() for word in words]:
                print('Wrong name, try again.')
                guess_word = input("Guess the Name: ")
                attempts += 1

            print(f'\tCongratulations! You won, You made {attempts} attempts')
            player_attempts.append(attempts)

            wanna_play = input('Do you want to continue playing? Enter yes or no: ')
            if wanna_play.lower() != 'yes':
                print('Alright, Nice game')
                break
            else:
                show_score(player_attempts)
                words = get_words()
                print(show_hint())

        except ValueError as err:
            print(err)
            print('Please provide valid inputs. Try Again!')

def show_score(attempts_records):
    if not attempts_records:
        print('No current high score,\nGive it a try')
    else:
        print(f'Current high score: {min(attempts_records)} attempts')

if __name__ == '__main__':
    begin_game()



            
            
            
              