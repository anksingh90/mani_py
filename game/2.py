# Programming Project: Casino Slot Machine (User vs System)

import random

user_wallet = 1000
sys_wallet = 1000

symbols = {1: 'Cherry', 2: 'Lemon', 3: 'Orange', 4: 'Star', 5: 'Diamond', 6: 'Seven', 7: 'Jackpot'}

print('\nWelcome to CASINO SLOT MACHINE')
print('------------------------------')
print('User Balance   : ',user_wallet ,'coins')
print('System Balance   : ',sys_wallet ,'coins')

# menu
while True:
    print('\n1. Single Spin Mode')
    print('2. Multi-Round Mode (Best of 5)')
    print('0. Exit\n')
    ch = int(input('Enter your choice: '))
    if ch == 1:
        print('\n--- SINGLE SPIN MODE ---')
        print('User Balance   : ',user_wallet ,'coins')
        print('System Balance   : ',sys_wallet ,'coins\n')

        # user bet
        user_bet_amt = int(input('Enter your bet amount: '))

        # system Bet (10% to 25% amt of wallet)
        lower_amt = int(0.1 * sys_wallet)
        upper_amt = int(0.25 * sys_wallet)
        sys_bet_amt = random.randint(lower_amt,upper_amt)
        print('System bets: ',sys_bet_amt)

        print('\nSpinning slots...\n')

        # Starting the spinning for user !
        user_slot = []
        for i in range(3):
            value = random.randint(1,7)
            user_slot.append(value)
        print('User Slots   : ', user_slot)

        # Starting the spinning for system !
        sys_slot = []
        for i in range(3):
            value = random.randint(1,7)
            sys_slot.append(value)
        print('System Slots   : ', sys_slot)

        # result evaluation + comparison + settlement of winner
        u_1 = user_slot[0]
        u_2 = user_slot[1]
        u_3 = user_slot[2]
        if u_1 == u_2 == u_3:
            user_bet_amt = user_bet_amt*10
            print('User wins this round!, Amount won : ', user_bet_amt)
        elif u_1 == u_2 or u_1 == u_3 or u_2 == u_3:
            user_bet_amt = user_bet_amt*3
            print('User wins this round!, Amount won : ', user_bet_amt)
        else:
            print('User loses ',user_bet_amt,' coins')
            
        # system status -
        s_1 = sys_slot[0]
        s_2 = sys_slot[1]
        s_3 = sys_slot[2]
        if s_1 == s_2 == s_3:
            user_bet_amt = user_bet_amt*10
            print('System wins this round!, Amount won : ', sys_bet_amt)
        elif s_1 == s_2 or s_1 == s_3 or s_2 == s_3:
            user_bet_amt = user_bet_amt*3
            print('System wins this round!, Amount won : ', sys_bet_amt)
        else:
            print('System loses ',sys_bet_amt,' coins')

    elif ch == 2:
        print('welcome')
    elif ch == 0:
        break
    else:
        print('Invalid Response ! Try Again.')
