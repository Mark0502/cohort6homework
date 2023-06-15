correct_pin = '3457'
max_attempts = 3
attemps = 0
attempts_left = 3
while attemps < max_attempts:
    supplied_pin = input("Enter your pin:")
    if supplied_pin == correct_pin:
        print('pin correct')
        break
    else:
        attemps += 1
        attempts_left = max_attempts - attemps
        print('pin incorrect - attempts left: ', attempts_left)
if attemps == max_attempts:
    print("Max attempts reached, card chewed and destroyed")