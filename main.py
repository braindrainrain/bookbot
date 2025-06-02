from stats import word_counter, lowercase, get_book_text, sorted_count_letters
content = get_book_text("books/frankenstein.txt")
word_count = word_counter(content)
lower_text = lowercase(content)
sorted_character_counts = sorted_count_letters(lower_text)
print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for char_data in sorted_character_counts:
    if char_data["char"].isalpha():
        print(f"{char_data["char"]}: {char_data["num"]}")
print("============= END ===============")
