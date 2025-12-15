from stats import number_of_words
from stats import count_characters
from stats import sorted_dictionaries

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    path = "books/frankenstein.txt"
    result = get_book_text(path)
    chars = count_characters(result)
    sorted_char_list = sorted_dictionaries(chars)
    num_words = number_of_words(result)
    print("============ BOOKBOT ============")
    print (f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print("Found", num_words, "total words")
    print("--------- Character Count -------")
    for item in sorted_char_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
        else:
            continue
    print("============= END ===============")

main()