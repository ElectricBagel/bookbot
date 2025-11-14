def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return (file_contents)

def book_list(booktxt):
    bklist = booktxt.split()
    word_count = len(bklist)
    return (word_count)

def text_count(booktxt):
    char_lower = booktxt.lower()
    char_list = set(char_lower)
    char_dict = {}
    for char in char_list:
        char_count = char_lower.count(char)
        char_dict[char] = char_count
    return char_dict


