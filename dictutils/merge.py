def merge(*textfiles):
    """
    Merges dictionary-like text files into one new file.
    Returns path to newly created file as string.

    *textfiles (string(s)): Path to text file(s).
    """
    if len(textfiles) == 1:
        raise Exception("merge requires at least 2 arguments, only 1 was given")
    newfile = "merge_dict.txt"
    with open(newfile, "w") as f:
        for file in textfiles:
            with open(file, "r") as oldfile:
                lines = oldfile.readlines()
                for word in lines:
                    f.write(word)
    return newfile
    