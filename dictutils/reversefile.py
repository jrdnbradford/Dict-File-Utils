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
    