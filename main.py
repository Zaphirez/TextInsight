import sys
from collections import Counter
import string

# Set output encoding to utf-8
sys.stdout.reconfigure(encoding='utf-8')

def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read().lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Count letters and words
    letter_count = Counter(c for c in text if c.isalpha())
    word_count = Counter(text.split())

    return letter_count, word_count

# Example usage
file_path = 'TEXT_HERE.txt'  # Change this to your actual file path
letter_count, word_count = analyze_text(file_path)

# Sort letter frequency and get top 3
top_3_letters = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)[:3]
print("Top 3 Letters:")
for letter, count in top_3_letters:
    print(f"The letter: \"{letter}\" got used {count} times.")

# Sort word frequency and get top 3
top_3_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:3]
print("\nTop 3 Words:")
for word, count in top_3_words:
    print(f"The word: \"{word}\" got used {count} times.")
