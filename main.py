def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    #print(file_contents)
    print(count_words(file_contents))
    count_unique_characters(file_contents)

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
    print(chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()