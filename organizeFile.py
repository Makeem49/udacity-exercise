import string

rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]

# My version of text processing


def check_word(word):
    # This check for rude line in the file
    if word in rude_words:
        for ch in word:
            if ch not in string.punctuation:
                word = word.replace(ch, "*")
    return word


def check_line(words):
    pos = 0
    for word in words:
        word = word.strip(string.punctuation).lower()
        filter_word = check_word(word)
        words[pos] = filter_word
        pos += 1
    return " ".join(words)


with open("my_contents.txt") as content:  # this happen first
    # The first context manager help to read and close the file
    with open('filter_doc.txt', 'w') as filter_word:
        for sentence in content:
            words = sentence.split(' ')
            filter_word.write(check_line(words))
