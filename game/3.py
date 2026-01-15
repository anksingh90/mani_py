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
        user_symbol = random.randint(0,1)
        if user_symbol == 0:
            user_symbol = 'X'
            sys_symbol = 'O'
        else:
            user_symbol = 'O'
            sys_symbol = 'X'
        
        board_lst = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

        print('\nStarting new game! You are', user_symbol ,'System is ',sys_symbol)
        print('You go first!')
        print('\nCurrent Board:')

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

        print('Position : 0 / 1 / 2 -->', end=' ')
        print('\t',board_lst[0][0], '|',board_lst[0][1],'|',board_lst[0][2])
        print('\t\t\t\t-----------')
        print('Position : 3 / 4 / 5 -->', end=' ')
        print('\t',board_lst[1][0], '|',board_lst[1][1],'|',board_lst[1][2])
        print('\t\t\t\t-----------')
        print('Position : 6 / 7 / 8 -->', end=' ')
        print('\t',board_lst[2][0], '|',board_lst[2][1],'|',board_lst[2][2])
        print(' ')
        

        '''
        for rows in range(3):

            for col in range(3):
                if col == 2:
                    continue
                else:
                    print(' '*4,end = '| ')
            if rows == 2:
                continue
            else:
                print('\n---------------')
        print('\n')
    '''
    elif ch == 2:
        print('ch == 2')
    
    elif ch == 0:
        break
    
    else:
        print('Invalid !')
