from stats import number_of_words
from stats import count_characters

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    path = "books/frankenstein.txt"
    result = get_book_text(path)
    chars = count_characters(result)
    num_words = number_of_words(result)
    print("Found", num_words, "total words")
    print(chars)

main()