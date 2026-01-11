import random

symbols = {1: 'Cherry', 2: 'Lemon', 3: 'Orange', 4: 'Star', 5: 'Diamond', 6: 'Seven', 7: 'Jackpot'}
wallet_user=1000
wallet_sys=1000

print("Welcome to CASINO SLOT MACHINE")
print('------------------------------')
print("User Balance   : ",wallet_user,' coins')
print("System Balance   : ",wallet_sys,' coins\n')
print('1. Single spin mode Game')
print('2. Multi Round Game (Best of 5)')
print('0. To Exit\n')
ch=int(input("Enter your choice : "))

user_slot=[]
system_slot=[]
if ch==1:
    print("--- SINGLE SPIN MODE ---\n")
    bet_user=int(input("Enter your bet more than 100 : "))

    # deducting value from user wallet !
    wallet_user = wallet_user - bet_user
    print("remaining wallet of user",wallet_user)
    # deducting value from system wallet !
    bet_sys = random.randint(100,250)
    print('\nSystem bets: ',bet_sys)
    wallet_sys = wallet_sys - bet_sys
    print("remaining wallet of sys",wallet_sys)

    print("\nSpinning slots...")

    # Generating slots for user & system
    for i in range(3):
        value=random.randint(1,7)
        user_slot.append(symbols[value])
    for i in range(3):
        guess=random.randint(1,7)
        system_slot.append(symbols[guess])
    
    print("\nUser Slots   : ",user_slot)
    print("System Slots : ",system_slot)
    
    user_final_score = 0
    sys_final_score = 0

    # user slot comparision
    if user_slot[0]==user_slot[1] or user_slot[1]==user_slot[2] or user_slot[0]==user_slot[2]:
        new_wallet=bet_user*3
        print('\nUser wins this round!')
        print("User wins ",new_wallet,"coins")            # fix the output - 'User wins 300 coins'
        wallet_user = wallet_user + new_wallet
        print(wallet_user)
        #print("User : Final balance :",new_wallet + wallet_user )
    elif user_slot[0]==user_slot[1]==user_slot[2]:
        new_wallet=bet_user*10
        print('\nUser wins this round!')
        print("updated wallet:",new_wallet)                # fix the output - 'User wins 300 coins'
        wallet_user = wallet_user + new_wallet
        print(wallet_user)
        #print("final balance of user:",new_wallet + wallet_user)
    else:
        new_wallet=bet_user*0
        print('\nUser Lost this round!')
        print("User : Updated Wallet :",wallet_user)        # fix the output - 'User lost 300 coins'
        #print("User : Final balance :", final_user)

    # system slot comparsion
    if system_slot[0]==system_slot[1] or  system_slot[1]==system_slot[2] or system_slot[0]==system_slot[2]:
        new_sys_wallet=bet_sys*3
        print('\nSystem wins this round!')
        print("System : updated wallet :",new_sys_wallet)       # fix the output - 'System wins 300 coins'
        wallet_sys = new_sys_wallet + wallet_sys
        print(wallet_sys)

        #print("final balance of sys:",new_sys_wallet + wallet_sys )
    elif system_slot[0]==system_slot[1]==system_slot[2]:
        new_sys_wallet=bet_sys*10
        print('\nSystem wins this round!')
        print("System : updated wallet :",new_sys_wallet)       # fix the output - 'System wins 300 coins'
        wallet_sys = new_sys_wallet + wallet_sys
        print(wallet_sys)
        #print("final balance of sys:",new_sys_wallet + wallet_sys)
    else:
        new_sys_wallet=bet_sys*0
        print('\nSystem Lost this round!')
        print("System : updated wallet :",new_sys_wallet)       # fix the output - 'System lost 300 coins'
        #print("System : final balance  :", final_sys)

    # Final balance update !
    print('\nUpdated Balances:')        
    print('User Balance   : ',wallet_user)
    print('System Balance   : ',wallet_sys)   
    if wallet_user>wallet_sys:
        print("**user wins**",wallet_user)
    else:
        print("**system wins**",wallet_sys)    


elif ch==2:
    count=0
    count_=0
    symbols = {1: 'Cherry', 2: 'Lemon', 3: 'Orange', 4: 'Star', 5: 'Diamond', 6: 'Seven', 7: 'Jackpot'}
    print("!!Multi spin mode!!")
    for i in range(5):
        user_slot=[]
        system_slot=[]
        print("Round :",i+1)
        print("**user bet**")
        bet_user=int(input("Enter your bet more than 100 : "))
        wallet_user = wallet_user - bet_user
        print("remaining wallet of user",wallet_user)
        # deducting value from system wallet !
        bet_sys = random.randint(100,250)
        print('\nSystem bets: ',bet_sys)
        wallet_sys = wallet_sys - bet_sys
        print("remaining wallet of sys",wallet_sys)

        print("\nSpinning slots...")
        for i in range(3):
                value=random.randint(1,7)
                user_slot.append(symbols[value])
        for i in range(3):
                guess=random.randint(1,7)
                system_slot.append(symbols[guess])
                
        print("\nUser Slots   : ",user_slot)
        print("System Slots : ",system_slot)
        if user_slot[0]==user_slot[1] or user_slot[1]==user_slot[2] or user_slot[0]==user_slot[2]:
                    new_wallet=bet_user*3
                    print('\nUser wins this round!')
                    print("User wins ",new_wallet,"coins")            # fix the output - 'User wins 300 coins'
                    wallet_user = wallet_user + new_wallet
                    print(wallet_user)
                        #print("User : Final balance :",new_wallet + wallet_user )
        elif user_slot[0]==user_slot[1]==user_slot[2]:
                    new_wallet=bet_user*10
                    print('\nUser wins this round!')
                    print("updated wallet:",new_wallet)                # fix the output - 'User wins 300 coins'
                    wallet_user = wallet_user + new_wallet
                    print(wallet_user)
                    #print("final balance of user:",new_wallet + wallet_user)
        else:
                    new_wallet=bet_user*0
                    print('\nUser Lost this round!')
                    print("User : Updated Wallet :",wallet_user)        # fix the output - 'User lost 300 coins'
                    #print("User : Final balance :", final_user)
            # system slot comparsion
        if system_slot[0]==system_slot[1] or  system_slot[1]==system_slot[2] or system_slot[0]==system_slot[2]:
                    new_sys_wallet=bet_sys*3
                    print('\nSystem wins this round!')
                    print("System : updated wallet :",new_sys_wallet)       # fix the output - 'System wins 300 coins'
                    wallet_sys = new_sys_wallet + wallet_sys
                    print(wallet_sys)

                    #print("final balance of sys:",new_sys_wallet + wallet_sys )
        elif system_slot[0]==system_slot[1]==system_slot[2]:
                    new_sys_wallet=bet_sys*10
                    print('\nSystem wins this round!')
                    print("System : updated wallet :",new_sys_wallet)       # fix the output - 'System wins 300 coins'
                    wallet_sys = new_sys_wallet + wallet_sys
                    print(wallet_sys)
                    #print("final balance of sys:",new_sys_wallet + wallet_sys)
        else:
                    new_sys_wallet=bet_sys*0
                    print('\nSystem Lost this round!')
                    print("System : updated wallet :",new_sys_wallet)       # fix the output - 'System lost 300 coins'
                    #print("System : final balance  :", final_sys)
        if wallet_sys>wallet_user:
                print("*system wins this round**",wallet_sys)
                count+=1
                print('final sys',count)
        else:
                print("**user wins this round",wallet_user)
                count_+=1
                print('final user',count_)
        if count>count_:
                print("**system wins**")
        else:
                print("**user wins**")

