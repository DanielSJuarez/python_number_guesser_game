from random import randint

turn = 1
print('Enter a number between 1 and 10, computer has 3 guesses to win!')
player = input('1,2,3,4,5,6,7,8,9,10 ')
play = True
min_num = 1
max_num = 10
computer = (min_num + max_num) // 2  #computer_number = (min_num + max_num) // 2  this floors and guesses 5 to split that guesses then. This is box section
#min_num, max_num = 1,10 

while play == True:

    if int(player) == computer:
        print(computer, 'Computer Win! It took this many turns', turn)
        play = False
    elif int(player) < computer:
        print(computer, 'Computer guessed High!')
        turn = turn + 1
        max_num = computer
    elif int(player) > computer:
        print(computer, 'Computer guessed Low!')
        turn = turn + 1
        min_num = computer
