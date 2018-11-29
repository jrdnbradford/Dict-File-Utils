def alphabetize(textfile):
    """
    Alphabetize words from text file and write words to new file. Returns path 
    to newly created file as string. 

    textfile (string): Path to text file.
    """
    
    with open(textfile, "r") as f:
        lines = f.readlines() 
        sorted_words = sorted(lines, key = str.lower) 
    
    newfile = f"alpha_{textfile}"
    with open(newfile, "w") as f:
        for word in sorted_words:
            f.write(word)
    return newfile
