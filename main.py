from stats import word_counter, lowercase, get_book_text, sorted_count_letters
content = get_book_text("books/frankenstein.txt")
word_count = word_counter(content)
print(f"There are {word_count} words in the document.")
lower_text = lowercase(content)
print(lower_text)
print(f"''t': {character_counters['t']}'")
print(f"''p': {character_counters['p']}'")
print(f"''c': {character_counters['c']}'")
sorted_character_counts = sorted_count_letters(character_counts)
for char_data in sorted_character_counts:
    if char_data["char"].isalpha():
        print(f"{char_data["char"]}:{char_data["num"]}")
