import Exercise_14


def play_again():

    play = input('!!!!!!Would you like to play again!!!!!! - y/n: ').lower()

    if play == 'y':
        print(' ')
        print('Good luck')
        print(' ')
        rock_paper_scissors()
    else:
        exit()
