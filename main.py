def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    print(get_book_text("frankenstein.txt"))


main()
