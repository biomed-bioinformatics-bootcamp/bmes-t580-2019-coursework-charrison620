import random
print('------------------------------------')
print('         Guess the Primer Game      ')
print('------------------------------------')
print()

goal = random.choice('ATGC')
for i in range(4):
    goal+= random.choice('ATGC')
guess = 'XXXXX'

name=input('Player what is your name? ')

while guess != goal:
    guess = input('Guess a 5 base pair primer:')

    incorrect = 0
    for i in range(len(guess)):
        if guess[i] != goal[i]:
            incorrect += 1

    if incorrect > 0:
        print('Sorry {}, you guessed {} bases wrong.'.format(name, incorrect))
    else:
        print('Excelent work {}, you won, it was {}!'.format(name,incorrect))

print('Done')



