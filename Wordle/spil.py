import nltk
nltk.download('words')

from nltk.corpus import words

# Get a list of English words
english_words = words.words()

# Filter words with exactly 5 letters
five_letter_words = [word.lower() for word in english_words if len(word) == 5]

# Print the list of 5-letter words
print(f'const dictionary = {five_letter_words};')
