"""
File: anagram.py
Name: Charlene
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
anagram_dic = []              # It's a dictionary storing words from a file


def main():
    """
    Read file into a dictionary and let users find anagrams of a word which should exist in the dictionary.
    """
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        # Determine when to quit finding anagrams
        if word == EXIT:
            break
        else:
            read_dictionary(FILE, word)
            start = time.time()
            find_anagrams(word)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(file, word):
    """
    Read a file into a dictionary.

    :param file: a string representing a file path
    :param word: a string representing a given word to look for anagrams
    """
    with open(file, 'r') as f:
        for line in f:
            # Add cleaned and relevant data into the dictionary
            if len(line.strip()) == len(word) and word[0] in line.strip() and word[len(word)-1] in line.strip():
                anagram_dic.append(line.strip())


def find_anagrams(s):
    """
    Find and display anagrams of a given word which should exist in the dictionary.

    :param s: a string representing a word to look for anagrams
    """
    anagram_list = []
    helper(list(s), 0, anagram_list, [False])
    print(f'{len(anagram_list)} anagrams: {anagram_list}')


def helper(s_list, level, anagram_list, is_searching):
    """
    Helper function of find_anagrams function.

    :param s_list: a list of string representing individual characters of a word to look for anagrams
    :param level: an int representing the index of an element in a list which should get swapped
    :param anagram_list: a list of anagrams for a given word
    :param is_searching: a list of a boolean value telling users whether the function is searching anagrams
    """
    if not is_searching[0]:
        print('Searching...')
        is_searching[0] = True
    # Determine base case where a swap is completed and the anagram exists in a dictionary
    if level == len(s_list):
        if ''.join(s_list) in anagram_dic and ''.join(s_list) not in anagram_list:
            print('Found: ' + ''.join(s_list))
            anagram_list.append(''.join(s_list))
            is_searching[0] = False
    # Determine recursive case where this function is called when swapping characters
    else:
        for j in range(level, len(s_list)):
            # Choose
            s_list[level], s_list[j] = s_list[j], s_list[level]
            # Facilitate the process of finding anagrams by checking a prefix
            # (PS Is there a more efficient way?)
            if has_prefix(s_list[:level + 1]):
                # Explore
                helper(s_list, level + 1, anagram_list, is_searching)
            # Un-choose
            s_list[level], s_list[j] = s_list[j], s_list[level]


def has_prefix(sub_s):
    """
    Consult a dictionary to see if there's a word with a given prefix.

    :param sub_s: a list of characters as prefix to check for existence in a dictionary
    :return: a boolean representing whether there's a word with a given prefix in a dictionary
    """
    prefix = ''.join(sub_s)
    for word in anagram_dic:
        if prefix == word[:len(prefix)]:
            return True


if __name__ == '__main__':
    main()
