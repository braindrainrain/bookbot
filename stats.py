def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def word_counter(text):
    word_list = text.split()
    count = len(word_list)
    return count


def main():
    book_text = get_book_text("books/frankenstein.txt")
    content = word_counter(book_text)
    print(f"{content} words found in the document")


def lowercase(text):
    text.lower(text)


main()
