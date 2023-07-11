import random


def rock_paper_scissors():

    selections = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    comp_selection_list = ['Rock', 'Paper', 'Scissors']

    user_input = input('Please choose for Rock, Paper or Scissors: ').lower()
    while user_input not in selections:
        print(' ')
        user_input = input(' Please select a valid input r ,p, s : ').lower()

    user_selection = selections[user_input]

    #if user_selection == 'd':
       # print (' Congratulations you win as dynamite destroys Rock,Paper,Scissors')
       # play_again()

    computer_selection = random.randint(0, 2)
    comp_choice = comp_selection_list[computer_selection]

    print('Your choice: ', user_selection)
    print('Computer Choice: ', comp_choice)

    if user_selection == comp_choice:
        print("It's a tie!")
        print(' ')
    elif user_selection == 'Rock' and comp_choice == 'Scissors':
        print("You Win as Rock blunts Scissors!")
        print(' ')
    elif user_selection == 'Paper' and comp_choice == 'Rock':
        print("You Win as Paper covers Rock!")
        print(' ')
    elif user_selection == 'Scissors' and comp_choice == 'Paper':
        print("You Win as Scissors cuts Paper!")
        print(' ')
    else:
        print("Sorry but the computer Wins as everthing it does is better!")
        print(' ')

    play_again = input('!!!!!!Would you like to play again!!!!!! - y/n: ').lower()

    if play_again == 'y':
        print(' ')
        print('Good luck')
        print(' ')
        rock_paper_scissors()
    else:
        exit()


rock_paper_scissors()
