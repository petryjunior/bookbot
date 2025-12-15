def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def number_of_words(result):
    words = result.split()
    num_words = len(words)
    return num_words

def main():
    path = "books/frankenstein.txt"
    result = get_book_text(path)
    num_words = number_of_words(result)
    print("Found", num_words, "total words")

main()