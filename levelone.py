from random import randint

turn = 3
guesses = randint(1,10)
play = True

while play == True: 
    print('Guess a number between 1 and 10, you have 3 guesses')
    player = input('1,2,3,4,5,6,7,8,9,10 ')
    computer = guesses

    if int(player) == computer:
        print('You Win!')
        play = False
    elif turn == 0:
        print('You Lose!')
        play = False
    elif int(player) < computer:
        print('To Low! ', turn, 'guess remaining!')
        turn = turn - 1
    elif int(player) > computer:
        print('To High! ', turn, 'guesses remaining!')
        turn = turn - 1

        