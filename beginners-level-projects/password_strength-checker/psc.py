import string
import getpass
import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Check if the password contains lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    else:
        remarks.append('Add lowercase letters.')

    # Check if the password contains uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        remarks.append('Add uppercase letters.')

    # Check if the password contains numbers
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        remarks.append('Add numbers.')

    # Check if the password contains special characters
    if any(char in string.punctuation for char in password):
        strength += 1
    else:
        remarks.append('Add special characters.')

    # Check if the password meets a minimum length requirement
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append('Make the password longer (at least 8 characters).')

    # Provide remarks based on password strength
    if strength == 1:
        remarks.insert(0, 'That\'s a very weak password. Change it as soon as possible.')
    elif strength == 2:
        remarks.insert(0, 'That\'s a weak password. You should consider using a stronger password.')
    elif strength == 3:
        remarks.insert(0, 'Your password is decent, but it can be improved.')
    elif strength == 4:
        remarks.insert(0, 'Your password is strong, but there is room for enhancement.')
    elif strength == 5:
        remarks.insert(0, 'Congratulations! Your password is very strong and secure.')

    return strength, remarks

def check_pwd():
    while True:
        password = getpass.getpass('Enter the password: ')
        strength, remarks = check_password_strength(password)
        print('Password Strength Analysis:')
        for remark in remarks:
            print(f'- {remark}')
        print(f'Password Strength Score: {strength} out of 5')

        choice = input('Do you want to check another password\'s strength (yes/no): ')
        if choice.lower() != 'yes':
            print('Exiting...')
            break

if __name__ == '__main__':
    print('===== Welcome to Password Strength Checker =====')
    check_pwd()
