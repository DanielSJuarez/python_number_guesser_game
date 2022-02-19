import math

print('Enter a number between 1 and 10, computer has 3 guesses to win!')
player = input('1,2,3,4,5,6,7,8,9,10 ')

turn = 1
play = True
low_number = 1
high_number = 10

while play == True:
    computer = math.floor((low_number + high_number) / 2)
    if int(player) == computer:
        print(computer, 'Computer Win! It took this many turns', turn)
        play = False
        break
    elif int(player) < computer:
        turn += 1
        high_number = computer - 1
        print(computer, 'Computer guessed High!')
        continue
    else:
        turn += 1
        low_number = computer + 1
        print(computer, 'Computer guessed Low!')
        continue
