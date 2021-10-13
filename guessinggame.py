import random

randomN= random.randint(1,20)
count = 1

print('''I am thinking of a number between 1 and 20. \nTake a guess.''')
user_input = int(input('User input: '))

while user_input != randomN:

    if user_input < randomN:
        print('Your guess is too low')

    if user_input > randomN:
        print('Your guess is too high')

    print('Take a guess')
    user_input = int(input('User Input: '))
    count= count + 1

    break
print('Good job! You guessed my number in ' + str(count) + ' guesses')
      


