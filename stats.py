def word_count(book_content):
    count = book_content.split()
    return len(count)

def count_letters(text):
    result = {}
    for c in text.lower():
        if 'a' <= c <= 'z':
            result[c] = result.get(c, 0) + 1
    return result

def dict_to_list(dict):
    res = []
    for letter in dict:
        res.append({"char": letter, "num": dict[letter]})
    return res

def sort_on(items):
    return items["num"]

def book_sort(dict):
    dict.sort(reverse=True, key=sort_on)
    return dict