#Numbers game
import random
import time

guessesTaken = 0

number = random.randint(1, 50)
print("Hey! I am thinking of a number between 1 and 50. Try to guess it.")


time.sleep(3)


while guessesTaken < 5:
    print('Take a guess.')
    guess = input()
    guess = int(guess)
    time.sleep(2)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('That number is too low dummy, guess higher!')

    if guess > number:
        print('You are too high dude, calm it down a bit')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('About time, you guessed my number in ' + guessesTaken + ' guesses...took you long enough!')

if guess != number:
    number =str(number)
    print('Sorry fam, the number i was thinking of was ' + number + '. Better luck next time dude.')