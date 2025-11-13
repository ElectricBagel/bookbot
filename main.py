def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return (file_contents)

def book_list(booktxt):
    bklist = booktxt.split()
    word_count = len(bklist)
    return (word_count)


def main():
    book_text = get_book_text("books/frankenstein.txt")
    book_count = book_list(book_text)
    print(f"Found {book_count} total words")

main()