def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    print(text)
    number_of_words = get_number_of_words(text)
    print(number_of_words)

def get_number_of_words(text):
    return len(text.split())


def get_book_path(path):
    with open(path) as f:
        return f.read()


if __name__ == '__main__':
    main()
