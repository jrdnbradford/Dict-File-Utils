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
            try:
                quicklist[idx[0]][idx[1]][idx[2]].append(word)
            except TypeError:
                #print("Dictionary get() method returned None.")
                quicklist[0][0][0].append(word)
    return quicklist


def get_index(word):
    """
    Returns a list of indices for the passed word.

    word (string): A word.
    """
    try:
        idx1 = char_dict.get(word[0])
        idx2 = char_dict.get(word[1])
        idx3 = char_dict.get(word[2])
    except IndexError:
        #print("Passed word is smaller than three characters.")
        try:
            idx2 = char_dict.get(word[1])
            idx3 = idx2
        except IndexError: 
            #print("Passed word is smaller than two characters.")
            try:
                idx3 = idx2 = idx1
            except Exception as err:
                print(err)  

    idx = [idx1, idx2, idx3]
    return idx
