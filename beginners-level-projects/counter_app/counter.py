import time

def countdown(user_time):
    while user_time >= 0:
        mins, secs = divmod(user_time, 60)  # Calculate minutes and seconds
        timer = '{:02d}:{:02d}'.format(mins, secs)  # Format time as 'mm:ss'
        print(timer, end='\r')  # Print the timer, overwriting the previous output
        time.sleep(1)  # Wait for 1 second
        user_time -= 1  # Decrease the remaining time by 1 second
    print('Odabo!')  # Display "Lift off!" when the timer reaches zero

if __name__ == '__main__':
    user_time = int(input("Enter a time in seconds: "))  # Get user input for the countdown time
    countdown(user_time)  # Start the countdown
