#Piotr Niedziałek
import unidecode
import re

def load_file(path, n):
    with open(
        path,
        "r",
        encoding="utf8",  # there was a problem, without "utf8", would not work
    ) as file:  # opening file from your working folder
        data = file.read()
    # list_of_words = data.split(maxsplit=n)
    data = data.lower()
    data=unidecode.unidecode(data)
    list_of_words = re.split("[^a-z]+", data, n)
    list_of_words.pop()  # we delete rest of words that we do not need
    # for i in range(0,len(list_of_words)):
    #     list_of_words[i]=re.sub(r'\W+', '', list_of_words[i])

    #print(list_of_words)
    return list_of_words
