# This code sample is inspired by the book "Gadsby" by
# Ernest Vincent Wright, which does not contain the
# letter "e".
#
# The purpose of this code is to validate a hypothesis
# that writing Gadsby was hard because "e" is the most
# commonly used letter in the English language. We
# test this by analyzing the character count of a single
# book.

infile = open('jane_eyre.txt')

# Make a list of all the characters in the book in order.
chars = []

# We do this by reading each line...
for line in infile:
    # ...cleaning it up...
    line = line.strip().lower()

    # ...then iterating over each character in the line, and
    # adding it to the chars list.
    for c in line:
        chars.append(c)

# Create an empty dictionary mapping each character to a count
# of how many times it appears in the book.
char_count = {}

# For each character...
for c in chars:
    # ...check if it exists in the dictionary.
    if c not in char_count:
        # If we have not encountered this character yet, give it a
        # count of 0.
        char_count[c] = 0
    
    # Increment the count of the character in the char_count dictionary
    char_count[c] = char_count[c] + 1

# Finally, output the dictionary. We can view character counts and
# determine which occurs the most frequently.
print(char_count)