from string import punctuation

def removepunc(textfile):
    """
    Remove all punctuation from words in text file and 
    write punctuationless words to new file. Returns 
    path to newly created file as string.
    
    textfile (string): Path to text file.
    """
    with open(textfile, "r") as f:
        lines = f.readlines()
        list_ = []
        for word in lines:
            for punc in punctuation:
                if punc in word:
                    word = word.replace(punc, "")
            list_.append(word.strip())

    newfile = f"no_punc_{textfile}"
    with open(newfile, "w") as f:
        for word in list_:
            f.write(f"{word}\n")
    return newfile
