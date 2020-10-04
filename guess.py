#Guessing game
from random import randint
x = randint(0,100)

print('Guess a number between 1 and 100: ')
guess = input()
xfound=0
num=0

while not xfound:
    num+=1
    if(int(guess)<x):
        print("Guess is less than the number. Try again: ")
        guess=input()
    elif(int(guess)>x):
        print("Guess is greater than the number. Try again: ")
        guess=input()
    else:
        print("It took you {} guesses but you got it!".format(num))
        xfound=1
