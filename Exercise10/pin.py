print('')                                        # This prints a blank line in run file to create a space so text is readable
print("Welcome to Scotland's bank of Mark")      # This prints bank welcome message
print('')                                        # again creates a blank line
correct_pin = '1867'                             # This defines 1867 as being the correct pin (string)
max_attempts = 3                                 # This creates variable max_attempts and defines the allowed attempts
attempts = 0                                     # This declares the starting attempts as being zero
attempts_left = 3                                # This lists the amount of attempts left starting variable
while attempts < max_attempts:                   # This says that while attempts is less than maximum attempt to:
    supplied_pin = input('Please input your four digit pin code: ')     # Prompt user for input and assigns it to supplied_pin
    print('')                                    # again creates a blank line
    if supplied_pin == correct_pin:              # This states that if user supplied pin is equal (==) to the correct pin to:
        print('pin correct')                     # Print that pin is correct
        break                                    # This breaks the run and ends the loop
    elif len(supplied_pin) > 4:                  # If the length of the code is more than 4 returns an error
        attempts += 1                            # This increases the attempts made by 1 increment
        attempts_left = max_attempts - attempts  # Attempts left is max attempts minus attempts
        print('You have entered your pin incorrect - you have', attempts_left, 'attempts left: ')   # Informs pin incorrect and lets user know how many attempts left
        print('')                                # again creates a blank line
        print('please input A "MAX" of 4 digits for your pin code')    # Informs user too many digits have been input
    else:                                        # else statement
        attempts += 1                            # This increases the attempts made by 1 increment
        attempts_left = max_attempts - attempts  # Attempts left is max attempts minus attempts
        print('You have entered your pin incorrect - you have', attempts_left, 'attempts left: ')   # Informs pin incorrect and lets user know how many attempts left
        print('')                                # again creates a blank line
if attempts == max_attempts:                     # This states that if the attempts is equal to the maximum amount of attempts:
    print("Max attempts reached: Were sorry but you cannot access your account") # Informs user max attempts made