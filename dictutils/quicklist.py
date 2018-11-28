"""
Module that supports high performance iterations 
against words in a dictionary-like text file.
"""

from string import printable

#Maps printable characters to list indices
char_dict = {letter: i for i, letter in enumerate(printable)}

def get_quicklist(textfile):
    """
    Appends words from a dictionary file to a returned 
    list using a list of indices returned by get_index(). 
    
    Results in much faster iterative searches for words as the word 
    can be searched for in a much smaller subsection of the dictionary.

    textfile (string): Path to text file.
    """
    #List of 100 lists each with 100 lists inside that each have 100 empty lists inside
    quicklist = [[[[] for i in printable] for i in printable] for i in printable] 

    with open(textfile, "r") as f:
        for word in f.readlines():
            word = word.strip()
            idx = get_index(word)
            quicklist[idx[0]][idx[1]][idx[2]].append(word)
    return quicklist


def get_index(word):
    """
    Returns a list of indices for the passed word.

    word (string): A word.
    """
    try:
        idx1 = char_dict[word[0]]
        idx2 = char_dict[word[1]]
        idx3 = char_dict[word[2]]
    except IndexError:
        #print(f"Passed word {word} is {len(word)} character(s).")
        try:
            idx2 = char_dict[word[1]]
            idx3 = idx2
        except IndexError: 
            #print(f"Passed word {word} is 1 character.")
            try:
                idx3 = idx2 = idx1
            except Exception as err:
                print(err) 
    except KeyError:
        #print(f"Unprintable character(s) in word: {word}.")
        idx3 = idx2 = idx1 = 0

    idx = [idx1, idx2, idx3]
    return idx
