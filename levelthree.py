from random import randint

turn = 1
print('Enter a number between 1 and 10, computer has 3 guesses to win!')
player = input('1,2,3,4,5,6,7,8,9,10 ')
play = True
computer = randint(1,10)

while play == True: 

    if int(player) == computer:
        print(computer, 'Computer Win! It took this many turn', turn)
        play = False
    elif int(player) < computer:
        print(computer, 'Computer guessed Low! ', turn, 'guess remaining!')
        turn = turn + 1
        computer = randint(1,computer)
    elif int(player) > computer:
        print(computer, 'Computer', turn, 'guesses remaining!')
        turn = turn + 1
        computer = randint(computer,10)