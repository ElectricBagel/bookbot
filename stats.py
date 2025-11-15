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

def _by_num(item):
    return item["num"]

def char_sort(char_2_sort):
    sort_on = []
    for c,n in char_2_sort.items():
        char_dicts = {
            "char": c,
            "num": n
                      }
        sort_on.append(char_dicts)
    #print(sort_on[:3])
    sort_on.sort(reverse=True, key=_by_num)
   
    return sort_on
    #print(f"Sorted Chars: {sorted_char}")
 #sorted_char = sorted(char_2_sort.keys())