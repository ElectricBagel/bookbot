def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return (file_contents)

def book_list(booktxt):
    bklist = booktxt.split()
    word_count = len(bklist)
    return (word_count)

