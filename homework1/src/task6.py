def count_words(filename):
    with open(filename, "r") as f:
        text = f.read()
    return len(text.split())

