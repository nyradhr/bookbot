def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    #print(file_contents)
    #print(count_words(file_contents))
    #print(count_unique_characters(file_contents))
    get_report(book_path, file_contents)

def count_words(text):
    words = text.split()
    return len(words)

def count_unique_characters(text):
    chars = {}
    for char in text:
        if char.lower() not in chars:
            chars[char.lower()] = 1
        else:
            chars[char.lower()] += 1
    return chars

def get_report(book_path, text):
    words = count_words(text)
    chars = count_unique_characters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document\n")
    for char in chars:
        if char.isalpha():
            print(f"The {char} character was found {chars[char]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()