import random

#define a function do shuffle all the characters of a string
def code(ctoken):
    codlist= list(ctoken)
    random.shuffle(codlist)
    return ''.join(codlist)

#generate a 6 digit code
number=str(random.randint(100000,999999)).zfill(6)

#assign the code to a variable
token = code(number)

print( ' Here is your 6 digit Code:' + token)


new_token = input('Enter your 6 digit code: ')
if new_token == token:
    print('Access Granted')

else:
    print('Access Denied')