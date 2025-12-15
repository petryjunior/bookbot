def number_of_words(result):
    words = result.split()
    num_words = len(words)
    return num_words

def count_characters(text):
    char_counts = {}
    for ch in text:
        ch = ch.lower()
        if ch in char_counts:
            char_counts[ch] += 1
        else:
            char_counts[ch] = 1
    return char_counts

def sorted_dictionaries(char_counts):
    my_list = []
    for char, num in char_counts.items():
        characters = {"char": char, "num": num}
        my_list.append(characters)
    my_list.sort(reverse=True, key=sort_on)
    return my_list

def sort_on(items):
    return items["num"]

        


