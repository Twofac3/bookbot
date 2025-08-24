def get_num_words(book):
    num = book.split()
    num_words = len(num)
    return num_words

def number_of_chars(book):
    char_count = {}
    for char in book.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_on(items):
    return items["num"]
    
def sort_char_count(char_count):
    result = []
    for char, count in char_count.items():
        result.append({"char": char, "num": count})
    result.sort(key=sort_on, reverse=True)
    return result
