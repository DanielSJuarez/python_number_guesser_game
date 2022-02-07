from random import randint

computerplayer = False
gameplayer = False
turn = 3
print('Do you want to guess, or be guessed?')
newselect = input('Guess, Be Guessed ')

if newselect == 'Guess':
    gameplayer = True
elif newselect == 'Be Guessed':
    computerplayer = True
    print('Enter a number between 1 and 10, computer has', turn, 'guesses to win!')
    player = input('1,2,3,4,5,6,7,8,9,10 ')


while computerplayer == True: 
    computer = randint(1,10)

    if int(player) == computer:
        print(computer, 'Computer Win!')
        computerplayer = False
    elif turn == 0:
        print('Computer Lose!')
        computerplayer = False
    elif int(player) < computer:
        print(computer, 'Computer guessed Low! ', turn, 'guess remaining!')
        turn = turn - 1
        computer = randint(1,computer)
    elif int(player) > computer:
        print(computer, 'Computer', turn, 'guesses remaining!')
        turn = turn - 1
        computer = randint(computer,10)



while gameplayer == True: 
    guesses = randint(1,10)
    computer = guesses
    print('Guess a number between 1 and 10, you have', turn, 'guesses remaining')
    player = input('1,2,3,4,5,6,7,8,9,10 ')

    if int(player) == computer:
        print('You Win!')
        gameplayer = False
    elif turn == 0:
        print('You Lose!')
        gameplayer = False
    elif int(player) < computer:
        print('To Low! ')
        turn = turn - 1
    elif int(player) > computer:
        print('To High! ')
        turn = turn - 1


 