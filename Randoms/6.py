# Game : Rock, Paper, Scissors

import random

print("***** Welcome to Game : ******")
print("--- Rock, Paper, Scissors: Best of 5 ---")

lst=["rock", "paper", "scissor"]
score_user = 0
score_sys=0

for i in range(5):
    print('--- Round',i,' ---')
    user_guess=input('User : Enter your choice (rock, paper, or scissor) : ').lower() # user input
    sys_guess=lst[random.randint(0,2)] # for computer
    if user_guess == sys_guess:
       print('Its a tie!')
       score_user = score_user + 0
       score_sys = score_sys + 0
       print('Scoreboard -> User: ', score_user ,'| Computer: ',score_sys)
    elif (user_guess=="rock" and sys_guess=="scissor") or (user_guess=="paper" and sys_guess=="rock") or (user_guess=='paper' and sys_guess=='scissor'):
        print('User wins this round !')
        score_user = score_user + 1
        print('Scoreboard -> User: ', score_user ,'| Computer: ',score_sys)
    elif user_guess != ('rock' or 'paper' or 'scissor'):
        print('Invalid Input !')
    else:
        print('System wins this round !')
        score_sys = score_sys + 1
        print('Scoreboard -> User: ', score_user ,'| Computer: ',score_sys)