from collections import defaultdict

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
