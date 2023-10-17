import os

def clear_screen():
    # Function to clear the console screen based on the operating system (Windows or other)
    os.system('cls' if os.name == 'nt' else 'clear')

def addition(history):
    # Addition operation
    print('Addition')
    ans = 0

    while True:
        num = float(input('Enter a number (or 0 to finish): '))
        if num == 0:
            break
        ans += num
        history.append(f'+ {num}')
        print(f'Current result: {ans}')

    return ans

def subtraction(history):
    # Subtraction operation
    print('Subtraction')
    ans = float(input('Enter the first number: '))
    history.append(str(ans))

    while True:
        num = float(input('Enter another number (or 0 to finish): '))
        if num == 0:
            break
        ans -= num
        history.append(f'- {num}')
        print(f'Current result: {ans}')

    return ans

def multiplication(history):
    # Multiplication operation
    print('Multiplication')
    ans = 1

    while True:
        num = float(input('Enter a number (or 1 to finish): '))
        if num == 1:
            break
        ans *= num
        history.append(f'* {num}')
        print(f'Current result: {ans}')

    return ans

def division(history):
    # Division operation
    print('Division')
    ans = float(input('Enter the first number: '))
    history.append(str(ans))

    while True:
        num = float(input('Enter another number (or 1 to finish): '))
        if num == 1:
            break
        while num == 0:
            num = float(input('Please enter a number greater than 0: '))
        ans /= num
        history.append(f'/ {num}')
        print(f'Current result: {ans}')

    return ans

def calculator():
    clear_screen()
    print('Simple Calculator in Python!')

    history = []

    while True:
        print('Select an operation:')
        print('Enter \'a\' for addition')
        print('Enter \'s\' for subtraction')
        print('Enter \'m\' for multiplication')
        print('Enter \'d\' for division')
        print('Enter \'h\' to view history')
        print('Enter \'q\' to quit')

        choice = input('Selection: ')

        if choice == 'q':
            break
        elif choice == 'a':
            result = addition(history)
            history.append(f'= {result}')
            print(f'Ans = {result}')
        elif choice == 's':
            result = subtraction(history)
            history.append(f'= {result}')
            print(f'Ans = {result}')
        elif choice == 'm':
            result = multiplication(history)
            history.append(f'= {result}')
            print(f'Ans = {result}')
        elif choice == 'd':
            result = division(history)
            history.append(f'= {result}')
            print(f'Ans = {result}')
        elif choice == 'h':
            if not history:
                print('No history available.')
            else:
                print('Operation History:')
                for entry in history:
                    print(entry)
        else:
            print('Sorry, invalid input. Try again.')

if __name__ == '__main__':
    calculator()
