def main():
    from random import randint
    f = open('wordlist.txt', 'r')
    allWords = f.read().split()
    guessthis = allWords[randint(0, len(allWords))]

    num_guesses = 10
    guessed_set = set()

    #Show rules and introduce
    print("Hi there! What's your name?")
    name = input()
    print("\nHi {}! Guess the following word:".format(name))
    for i in range(0, len(guessthis)):
        print("_", end=" ")
    print("\nIt has {} letters , and you have 10 wrong attempts to guess it!\n".format(len(guessthis)))
    print("Also, at any point if you think you have the whole word, go ahead and type it in \"I got it\" to put the word in.")
    print("BUT if you get the whole word wrong, all your attempts are done!")

    while True:
        letters_guessed = 0

        #Take a letter in
        print("\n\nEnter a letter: ")
        letter = input()
        if letter == "I got it":
            guessWholeWord(guessthis)
            break

        #Process the input
        if letter in guessthis:
            guessed_set.add(letter)
            print("That's in there!\n")
        else:
            num_guesses -= 1
            print("Guess again. You have {} guesses left\n".format(num_guesses))

        #Show progress to user
        for i in guessthis:
            if(i in guessed_set):
                letters_guessed += 1
                print(i, end=" ")
            else:
                print("_", end=" ")

        #End appropriately
        if(len(guessthis) == letters_guessed):
            print("\nYay! You guessed the word!")
            break
        if(num_guesses == 0):
            print("\nOops! You ran out of tries!")
            print("Here's the word: " + guessthis)
            break

def guessWholeWord(guessthis):
    print("\nWhat do you think the word is?")
    word = input()
    if word.lower() == guessthis:
        print("You got it!")
    else:
        print("Oops! You missed it!")
        print("Here's the word: " + guessthis)

main()
