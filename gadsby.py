# This code sample is inspired by the book "Gadsby" by
# Ernest Vincent Wright, which does not contain the
# letter "e".
#
# The purpose of this code is to search through our
# wordlist.txt file, and count the number of words
# which do not contain "e".

infile = open('words.txt')

words = []

# Mapping step: Read words from the file, and add them
# to the words list.
for line in infile:
    words.append(line)

# Mapping step: Clean up input words by removing whitespace
# (the newline character)
words_stripped = []
for w in words:
    w = w.strip()
    words_stripped.append(w)

# Filtering step: Remove words with an e
legal_words = []
for w in words_stripped:
    if 'e' not in w:
        legal_words.append(w)


# Reduction steps: Count the number of words in each list
print("Words without e: " + str(len(legal_words)))
print("Total words: " + str(len(words_stripped)))