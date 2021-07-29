"""
File: hangman.py
Name: Charlene
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Create an interactive word guessing game where a random word is set to let users guess.
    """
    answer = random_word()
    guess_system(answer, N_TURNS)


def guess_system(word, times):
    """
    :param word: The randomly generated word to be guessed, a string type.
    :param times: The times users can guess, an int type.
    Display the guessing process of this game.
    """
    memory_space = ''
    for ch in word:
        memory_space += '_'
    print('The word looks like ' + memory_space + '.')
    print('You have ' + str(N_TURNS) + ' guess(es) left.')
    count = 1
    while True:
        # The following directly makes an input case-insensitive.
        input_ch = input('Your guess: ').upper()

        # The following prevents any un-authoritative input.
        while True:
            if not input_ch.isalpha():
                print('illegal format.')
                # The following directly makes an input case-insensitive.
                input_ch = input('Your guess: ').upper()
            elif len(input_ch) > 1:
                print('illegal format.')
                # The following directly makes an input case-insensitive.
                input_ch = input('Your guess: ').upper()
            else:
                break

        # The following memorizes previous guess results.
        revealed_word = ''
        for i in range(len(word)):
            if input_ch == word[i]:
                revealed_word += input_ch
            else:
                revealed_word += memory_space[i]
        memory_space = revealed_word

        if input_ch in word:
            print('You are correct!')
            if revealed_word.isalpha():
                print('You win :)')
                break
            else:
                print('The word looks like ' + revealed_word + '.')
                print('You have ' + str(N_TURNS - count + 1) + ' guess(es) left.')
        else:
            print('There is no ' + input_ch + '\'s in the word.')
            if count < times:
                print('The word looks like ' + revealed_word + '.')
                print('You have ' + str(N_TURNS - count) + ' guess(es) left.')
            else:
                print('You are completely hung :(')
                break
            count += 1
    print('The word was: ' + word)


def random_word():
    """
    Generate a random word.
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
