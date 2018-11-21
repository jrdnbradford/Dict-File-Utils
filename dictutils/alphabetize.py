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
