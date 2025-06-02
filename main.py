from stats import word_counter, lowercase, get_book_text, sorted_count_letters
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
content = get_book_text(sys.argv[1])
word_count = word_counter(content)
lower_text = lowercase(content)
sorted_character_counts = sorted_count_letters(lower_text)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for char_data in sorted_character_counts:
    if char_data["char"].isalpha():
        print(f"{char_data["char"]}: {char_data["num"]}")
print("============= END ===============")
