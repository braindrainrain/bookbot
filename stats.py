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
    character_counts = {}
    lowercase_text = text.lower()
    for lowercase_count in lowercase_text:
        if lowercase_count in character_counts:
            character_counts[lowercase_count] += 1
        else:
            character_counts[lowercase_count] = 1
    return character_counts


def sort_on(dict):
    return dict["num"]


def sorted_count_letters(letters):
    dict_list = []
    for letter in letters:
        count_value = letters[letter]
        character_dict = {"char": letter, "num": count_value}
        dict_list.append(character_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
