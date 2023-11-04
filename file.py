def load_file(path, n):
    with open(
        path, "r", encoding="utf8" # there was a problem, without "utf8", would not work
    ) as file:  # opening file from your working folder
        data = file.read()
    list_of_words = data.split(maxsplit=n)
    list_of_words.pop() # we delete rest of words that we do not need
    return list_of_words