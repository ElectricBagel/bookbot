from stats import get_book_text
from stats import book_list
from stats import text_count

def main():
    
    book_text = get_book_text("books/frankenstein.txt")
    book_count = book_list(book_text)
    letter_count = text_count(book_text)
    print(f"Found {book_count} total words")
    print(letter_count)

main()