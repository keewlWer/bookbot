def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    print(text)
    number_of_words = get_number_of_words(text)
    print(number_of_words)
    number_of_characters = get_chars_dict(text.lower())
    print(number_of_characters)

def get_chars_dict(lowered_text):
    chars = {}
    for c in lowered_text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def get_number_of_words(text):
    return len(text.split())


def get_book_path(path):
    with open(path) as f:
        return f.read()


if __name__ == '__main__':
    main()
