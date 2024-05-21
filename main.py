def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_letters(book_text):
    char_dict = {}
    for char in book_text:
        lowered_char = char.lower()
        if lowered_char in char_dict:
            char_dict[lowered_char] += 1
        else:
            char_dict[lowered_char] = 1
    return char_dict

#Sort the character list dictionary on the number field
def sort_on(dict):
    return dict["num"]

#This function takes a character dictionary and creates a list of dictionaries
#This list of dictionaries will only be of alpha characters and have the key pairs: char and num
#The list will then be sorted by the number field in decending order (Highest to Lowest)
def get_alpha_char_list_sorted_by_number(char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            new_char_dict = {"char": char, "num": char_dict[char]}
            char_list.append(new_char_dict)
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list

def print_report(book_path, num_words, sorted_char_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")

    for list_dict in sorted_char_list:
        print(f"The '{list_dict["char"]}' character was found {list_dict["num"]} times")

    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_num_letters(text)
    sorted_char_list = get_alpha_char_list_sorted_by_number(char_dict)
    print_report(book_path, num_words, sorted_char_list)

main()