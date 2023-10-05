import random

attempts_records=[]

def show_score():
  if not attempts_records:
      print('No current high score,\nGive it a try')  
  else:
      print(f'Current high score:' f'{min(attempts_records)} attempts')
      
def start_game():
    attempts=0
    secret_number=random.randint(1,25)
    print('Welcom to the world of guesses!')
    player_name=input('What is the guesser\'s name:')
    ready=input(f'Hi {player_name}! '  f'wanna play? Enter(Yes/No)')
    
    if ready.lower() != 'yes':
        print('Wrong option, input either yes/no or Yes/No')
        exit()
    else:
        show_score()    

    while ready.lower() == 'yes':
        try:
            guess= int (input("Enter the number between 1 and 25:"))
            if guess <1 or guess>25:
                raise ValueError('Enter a number within the range')
            
            attempts =+ 1
            
            if guess == secret_number :
                print(f'Et Fabolouso')
                print(f'It took you {attempts} attempts')
                attempts_records.append(attempts)
                ready = input(f'{player_name} you wanna continue playing' f'Enter(Yes/No)')
                if ready.lower() != 'yes':
                    print('Excellent, Thanks for playing')
                    break
                else:
                    attempts=0
                    secret_number=random.randint(1,25)
                    show_score()
                    continue
            else:
                if guess > secret_number:
                    print ('Too High! Try again.')
                elif guess<secret_number:
                    print ('Too Low! Try again.')
                    #print ("You have", + str(3-attempt), "more chances left")
        except ValueError as err:
            print ('!!!That is not a valid input.......Try again')
            print (err)
            
if __name__ == '__main__':
    start_game()            
            
            
        
        
      
              
        