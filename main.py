import sys
from stats import get_num_words, number_of_chars, sort_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    # Read book text once
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")

    # Counts words and print
    word_count = get_num_words(book)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    # Count characters and print
    char_count = number_of_chars(book)
    print("--------- Character Count -------")
    sorted_chars = sort_char_count(char_count)
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
