from stats import get_book_text
from stats import book_list
from stats import text_count
from stats import char_sort
import sys

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        print(sys.argv)
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    book_count = book_list(book_text)
    letter_count = text_count(book_text)
    sorted_list = char_sort(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {book_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        ch = item["char"]
        if ch.isalpha() and ch in "abcdefghijklmnopqrstuvwxyz":
            print(f"{ch}: {item['num']}")
    print("============= END ===============")
main()