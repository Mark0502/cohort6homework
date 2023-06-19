from getpass import getpass

print('')
print("Welcome to Scotland's bank of Mark")
print('')
correct_pin = '1867'
max_attempts = 3
attempts = 0
attempts_left = 3
while attempts < max_attempts:
    supplied_pin = getpass(prompt='Please input your four digit pin code: ')
    print('')
    if supplied_pin == correct_pin:
        print('pin correct')
        break
    elif len(supplied_pin) > 4:
        attempts += 1
        attempts_left = max_attempts - attempts
        print('You have entered your pin incorrect - you have', attempts_left, 'attempts left: ')
        print('')
        print('please input A "MAX" of 4 digits for your pin code')
    else:
        attempts += 1
        attempts_left = max_attempts - attempts
        print('You have entered your pin incorrect - you have', attempts_left, 'attempts left: ')
        print('')
if attempts == max_attempts:
    print("Max attempts reached: Were sorry but you cannot access your account")

