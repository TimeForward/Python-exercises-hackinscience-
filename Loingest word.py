# Write a function giving the longest word in a given text.

# Your function should be named longest_word, take a single argument text and return a string which should be the longest word in the given text.

# Beware: the given text can span several lines.

# Example
# >>> longest_word("We want a SHRUBBERY")
# "SHRUBBERY"
# >>> longest_word("Shrubberies are great")
# "Shrubberies"
# Advice
# Read the documentation of the len builtin function.
def longest_word(text):
    split_text=text.split()
    x=''
    for i in split_text:
        if len(i)>len(x):
            x=i
    return x
