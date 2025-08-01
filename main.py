from stats import word_count
from stats import count_letters
from stats import book_sort
from stats import dict_to_list
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents





def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_content = get_book_text(filepath)
    cont_of_words = word_count(book_content)
    count_of_letters = count_letters(book_content)
    dict_letters = dict_to_list(count_of_letters)
    sorted_dict = book_sort(dict_letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {cont_of_words} total words ")
    print("--------- Character Count -------")
    for i in range(len(sorted_dict)):
        if not sorted_dict[i]["char"].isalpha()  :
            continue
        print(f"{sorted_dict[i]["char"]}: {sorted_dict[i]["num"]} ")

    print("============= END ===============")



main()