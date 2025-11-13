from stats import get_book_text
from stats import book_list

def main():

    book_text = get_book_text("books/frankenstein.txt")
    book_count = book_list(book_text)
    print(f"Found {book_count} total words")

main()