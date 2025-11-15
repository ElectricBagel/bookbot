from stats import get_book_text
from stats import book_list
from stats import text_count
from stats import char_sort

def main():
    
    book_text = get_book_text("books/frankenstein.txt")
    book_count = book_list(book_text)
    letter_count = text_count(book_text)
    sorted_list = char_sort(letter_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {book_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        ch = item["char"]
        if ch.isalpha() and ch in "abcdefghijklmnopqrstuvwxyz":
            print(f"{ch}: {item['num']}")
    print("============= END ===============")
main()