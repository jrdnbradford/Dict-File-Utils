def removedupes(textfile):
    """
    If there are duplicates in given text file, 
    remove them and write the result unordered 
    to new file, returning path to newly created 
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
