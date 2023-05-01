import random
import sys
import re

while True:
    print('\n')
    print('Rock, Paper, Scissor Game!')

    playerTurn = input('Choose your weapon! (R)ock / (P)aper / (S)cissor: ')

    if(not re.match('[RrPpSsEe]', playerTurn)) or (len(playerTurn) !=1):
        print('Invalid Input! Choose a letter (R/P/S/E)!: ')    
        continue

    #Exit
    if (playerTurn.upper() == 'E'):
        print('Exiting Game..')
        sys.exit

    #Player Choice
    print('You Choose: '+ playerTurn.upper())

    #list choices
    choises = ['R', 'P', 'S']

    #computer
    computerTurn = random.choice(choises)

    print('I Choose: '+ computerTurn)

    if playerTurn.upper() == computerTurn:
        print('Draw!')
        
    elif playerTurn.upper() == 'R' and computerTurn == 'S':
        print('Rock beat Scissor! You Win!')
        
    elif playerTurn.upper() == 'P' and computerTurn == 'R':
        print('Paper beat Rock! You Win!')
        
    elif playerTurn.upper() == 'S' and computerTurn == 'P':
        print('Scissor beat Paper! You Win!')
        
    else:
        print('You Lose!')