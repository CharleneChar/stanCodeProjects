"""
File: boggle.py
Name: Charlene
----------------------------------------
This program finds valid words from a 4*4 boggle
where inputs inside are given from users (using Trie).
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


# Create a Trie structure with tree nodes for valid words (from a dictionary)
class TreeNode:
    """
    A node in a trie.
    """
    def __init__(self, letter):
        """
        Set the node to contain a letter, a reference for another node,
        and a boolean value representing where the node is the last one in a trie.

        :param letter: a string representing a letter which will get stored in a node
        """
        self.letter = letter
        self.branches = {}
        self.leaf = False


class Trie:
    """
    A trie structure (representing a giant tree).
    """
    def __init__(self):
        """
        Set the trie to contain a root node of class TreeNode, which has a special character *.
        """
        self.root = TreeNode('*')

    def link_nodes(self, word):
        """
        Link nodes ,containing letters from a word, to the trie.

        :param word: a string where each letter would be turn into a node
        """
        cur_node = self.root
        for letter in word:
            if letter not in cur_node.branches:
                cur_node.branches[letter] = TreeNode(letter)
            cur_node = cur_node.branches[letter]
        cur_node.leaf = True


def main():
    """
    Let user create a 4*4 boggle by entering letter inputs under the following limits and
    search, Find out, display and record valid words within the boggle.

    Input limits include that there should be same amount of inputs in each row and with space
    inserted between any two input in a row, and every input should be just one letter from
    English alphabet.
    """
    stop = False
    data = []
    # Get boggle input data from users and arrange them into a matrix
    for i in range(4):
        data.append([ch for ch in input(f'{i + 1} row of letters: ').lower().split()])
        if len(data[i]) != 4 or len(''.join(data[i])) != 4:
            print('Illegal input')
            stop = True
            break
    # Execute the lookup process when there's no illegal input
    if not stop:
        start = time.time()
        # Pack the dictionary trie with input as an argument for boggle game solver function
        dictionary_trie = read_dictionary(data)
        data.append(dictionary_trie)
        game_sol(data)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your boggle algorithm: {end - start} seconds.')


def game_sol(data):
    """
    Search, Find out, display and record valid words
    (each of which should have longer than 4 letters and should exist in a specific dictionary)
    within a given boggle.

    :param data: a list of given letter inputs for boggle and a dictionary trie
    """
    trie = data[4]
    # Create a matrix to record trace while going through input
    trace = []
    for i in range(4):
        trace.append([])
        for j in range(4):
            trace[i].append(False)
    # Record the number of words from boggle
    lst = []
    # Start the lookup process with every input data as the first letter
    for i in range(4):
        for j in range(4):
            # Check if the input as the first letter is in the second level of the giant tree
            if data[j][i] in trie.root.branches:
                game_sol_helper(trie.root, data[:4], i, j, trace, data[j][i], '', lst)
    print(f'There are {len(lst)} words in total.')


def game_sol_helper(dict_trie_node, boggle, index_x, index_y, trace, cur_letter, s, lst):
    """
    A Helper function for game_sol function.

    :param dict_trie_node: a TreeNode containing special character or letter of a word
    :param boggle: a list containing strings of letter inputs given by users
    :param index_x: an int representing the row position of a letter in the boggle
    :param index_y: an int representing the column position of a letter in the boggle
    :param trace: a list of boolean values, each of which represents whether a letter is explored or not
    :param cur_letter: a string of current letter from the boggle
    :param s: a string of letters in a TreeNode existing in the giant tree, Trie
    :param lst: a list of valid words found within the boggle
    """
    # Print and record every final word when reach the bottom of a branch
    if dict_trie_node.leaf and s not in lst:
        print('Found \"' + s + '\"')
        lst.append(s)
    # Mark trace
    trace[index_y][index_x] = True
    # Explore in one of the eight directions from the current letter position
    for i in [[-1, -1], [-1, 1], [-1, 0], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        # Search along branches of the giant tree
        for parent, children in dict_trie_node.branches.items():
            # Check if the direction is in range and the function hasn't explored
            if 0 <= index_x + i[0] <= 3 and 0 <= index_y + i[1] <= 3 \
                    and not trace[index_y + i[1]][index_x + i[0]]:
                # Check if a letter in the current position is a node along a branch
                if cur_letter == parent:
                    # Recurse with children of the current node as new current node
                    game_sol_helper(children, boggle, index_x + i[0], index_y + i[1], trace,
                                    boggle[index_y + i[1]][index_x + i[0]], s + parent, lst)
    # Un-mark trace
    trace[index_y][index_x] = False


def read_dictionary(data):
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list

    :param data: a list of given letter inputs for boggle
    :return: a Trie of valid words (sifted) from the external dictionary file
    """
    lst = {}
    for row in data:
        for col in row:
            lst[col] = 1
    dictionary = {}
    trie = Trie()
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip().lower()
            # Get a smaller portion of the whole dictionary which contains only words with
            # letters which we get as Boggle input data from users, and Link letters of words
            # in the smaller portion of dictionary to complete one giant tree
            if word not in dictionary and 16 >= len(word) >= 4:
                for i in range(0, len(word)//4+1, 4):
                    if word[i] not in lst or word[i+1] not in lst \
                            or word[i+2] not in lst or word[i+3] not in lst \
                            or word[-(i + 1)] not in lst or word[-(i + 2)] not in lst \
                            or word[-(i+3)] not in lst or word[-(i+4)] not in lst:
                        break
                else:
                    dictionary[word] = 1
                    trie.link_nodes(word)
    return trie


if __name__ == '__main__':
    main()
