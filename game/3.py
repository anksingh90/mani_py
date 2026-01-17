# Tic-Tac-Toe

import random

while True:
    print('----- Main Menu : -----')
    print('1. Play Game, Single Round ')
    print('2. Play Game, Muti Round ')
    print('0. Exit \n')
    
    ch = int(input('Your choice: '))

    if ch == 1:
        # Assigning Symbol randomly to user & system !
        
        board_lst = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

        print('\nStarting new game! You are : X ; System is : O')
        print('You go first!')
        print('\nCurrent Board:')

        for round in range(8):

            print('Position : 0 / 1 / 2 -->', end=' ')
            print('\t',board_lst[0][0], '|',board_lst[0][1],'|',board_lst[0][2])
            print('\t\t\t\t-----------')
            print('Position : 3 / 4 / 5 -->', end=' ')
            print('\t',board_lst[1][0], '|',board_lst[1][1],'|',board_lst[1][2])
            print('\t\t\t\t-----------')
            print('Position : 6 / 7 / 8 -->', end=' ')
            print('\t',board_lst[2][0], '|',board_lst[2][1],'|',board_lst[2][2])
            print(' ')
            user_ch = int(input('Enter position to play : '))  # user input position

            if user_ch == 0:
                board_lst[0][0] = 'X'
            elif user_ch == 1:
                board_lst[0][1] = 'X'
            elif user_ch == 2:
                board_lst[0][2] = 'X'

    elif ch == 2:
        print('ch == 2')
    
    elif ch == 0:
        break
    
    else:
        print('Invalid !')
