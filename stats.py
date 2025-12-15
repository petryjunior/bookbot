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


