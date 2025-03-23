from stats import get_num_words, get_chars_count, sort_char_by_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

if len(sys.argv) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    path = sys.argv[1]
    book_text = get_book_text(path)

    word_count = get_num_words(book_text)
    char_count_dict = get_chars_count(book_text)
    sorted_chars = sort_char_by_count(char_count_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for char_info in sorted_chars:        
        char = char_info['char']
        count = char_info['count']
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


main()


    
