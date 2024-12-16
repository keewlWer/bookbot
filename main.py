

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    print(text)
    number_of_words = get_number_of_words(text)
    print(number_of_words)
    number_of_characters = get_chars_dict(text.lower())
    print(number_of_characters)
    print_a_report(book_path, number_of_words, number_of_characters)


def sort_on(dictionary, c):
    return dictionary[c]


def print_a_report(book_path, number_of_words, dict_of_numbers):
    # Step 1: Convert the dictionary to a list of dictionaries
    char_list = [{'char': k, 'num': v} for k, v in dict_of_numbers.items() if k.isalpha()]

    # Step 2: Sort the list based on 'num'
    char_list.sort(reverse=True, key=lambda x: x['num'])

    # Step 3: Print the sorted list
    print(f"--- Beginning report of {book_path} ---\n"
          f"{number_of_words} words found in the document\n")
    for entry in char_list:
        print(f"The '{entry['char']}' character was found {entry['num']} times")
    print("--- End report ---")


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
