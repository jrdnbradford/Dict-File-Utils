"""
Module that includes functions for manipulating 
and creating dictionary-like text files.
"""

from collections import defaultdict
from string import punctuation


def alphabetize(textfile):
    """
    Alphabetize words from text file and write words to new file. Returns path 
    to newly created file as string. 

    textfile (string): Path to text file.

    WARNING: if the same word appears more than once in the passed dictionary, 
    the duplicates will be removed even if they have different capitalizations 
    and only the capitalization of the last one in the given dictionary will be 
    preserved.
    """
    
    with open(textfile, "r") as f:
        lines = f.readlines()
        #Lowercase required for alphabetical sort
        #track_caps tracks whether word.lower() was formerly capitalized
        track_caps = {word.lower(): bool(word[0].isupper()) for word in lines}
        sorted_words = sorted(track_caps.keys()) 
    
    newfile = f"alpha_{textfile}"
    with open(newfile, "w") as f:
        for word in sorted_words:
            #Write capitalization preserved in track_caps
            if track_caps.get(word):
                word = word.capitalize()
            f.write(word)
    if len(lines) != len(track_caps.keys()):
        print(f"{len(lines) - len(track_caps.keys())} words in the file were not written to the new file.") 
    return newfile



def countletters(textfile, trackcaps = False):
    """
    Take in text file and return defaultdict with letters as keys 
    and the number of times a word beginning with that letter 
    appears as values.

    textfile (string): Path to text file.

    trackcaps (boolean): Optional kwarg that designates whether 
    the returned defaultdict will have both capitals and lowercases 
    as keys. Defaults to False.
    """
    lettercounter = defaultdict(int)
    with open(textfile, "r") as f:
        lines = f.readlines()
        words = [word if trackcaps else word.lower() for word in lines]     
        for word in words:
            lettercounter[word[0]] += 1
    return lettercounter



def removedupes(textfile):
    """
    If there are duplicates in given text file, 
    remove them and write the result unordered 
    to new file, returing path to newly created 
    file as string. If there are no duplicates,
    return None without writing a new file.

    textfile (string): Path to text file.
    """
    with open(textfile, "r") as f:
        lines = f.readlines()
        words = {word for word in lines}
        if len(lines) == len(words):
            print(f"There were no duplicates in {textfile}.")
            return

    newfile = f"no_dupes_{textfile}"
    with open(newfile, "w") as f:
        for word in words:
            f.write(word)
    return newfile



def removepunc(textfile):
    """
    Remove all punctuation from words in text file and 
    write punctuationless words to new file. Returns 
    path to newly created file as string.
    
    textfile (string): Path to text file.
    """
    with open(textfile, "r") as f:
        lines = f.readlines()
        _list = []
        for word in lines:
            for punc in punctuation:
                if punc in word:
                    word = word.replace(punc, "")
            _list.append(word.strip())

    newfile = f"no_punc_{textfile}"
    with open(newfile, "w") as f:
        for word in _list:
            f.write(f"{word}\n")
    return newfile



def reversefile(textfile):
    """
    Writes words in text file in reverse order to new file.
    Returns path to newly created file as string.

    textfile (string): Path to text file.
    """
    with open(textfile, "r") as f:
        lines = f.readlines()
        words = [word for word in lines][::-1]
    
    newfile = f"reversed_{textfile}"
    with open(newfile, "w") as f:
        for word in words:
            f.write(word)
    return newfile
