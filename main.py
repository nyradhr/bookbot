def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    print_report(book_path, file_contents)

def count_words(text):
    words = text.split()
    return len(words)

def get_characters_dict(text):
    chars = {}
    for char in text:
        if char.lower() not in chars:
            chars[char.lower()] = 1
        else:
            chars[char.lower()] += 1
    return chars

def print_report(book_path, text):
    words = count_words(text)
    chars = get_characters_dict(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document\n")
    alpha_chars = filter_alphabetic(chars)
    dict_list = sort_by_occurrence(alpha_chars)
    for dict in dict_list:
        print(f"The '{dict["key"]}' character was found {dict["value"]} times")
    print("--- End report ---")

def get_dict_list(dict):
    dict_list = []
    for key in dict:
        tmp = {"key": key, "value": dict[key]}
        dict_list.append(tmp)
    return dict_list

def filter_alphabetic(chars):
    alphabetic_dict = {}
    for char in chars:
        if char.isalpha():
            alphabetic_dict[char] = chars[char]
    return alphabetic_dict

def sort_by_occurrence(chars):
    dict_list = get_dict_list(chars)
    dict_list.sort(reverse=True, key=sort_on_value)
    return dict_list

def sort_on_value(dict):
    return dict["value"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()