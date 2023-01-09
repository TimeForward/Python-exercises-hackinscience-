# Print every pair of distinct letters
# Created by Julien Palard
# Provide a script printing every possible pairs of two different letters.

# Only lower case, one pair per line, ordered alphabetically.

# Don't print pairs consisting of twice the same letter, such as 'aa', 'bb', etc...

# So your output should look like:

# $ python3 solution.py
# ab
# ..
# az
# ba
# bc
# ,,
# zy
import string
alphabet=list(string.ascii_lowercase)
for i in alphabet:
    for j in alphabet:
        if i!=j:
            print (i+j)
