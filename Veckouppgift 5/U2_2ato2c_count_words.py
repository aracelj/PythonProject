"""

2a:
Requirements:
     1. Input an empty string
     2. Inputs a string separated with comma
     3. Inputs a mix string composed of numbers or words or characters and counts it as one word if separated by a comma
     4. Returns the count as an integer
Acceptance Criteria:
     Accepts an empty string and returns None.
     Accepts a string with no comma, returns one word
     Accepts a a mixed string separated by a space, it counts as a word when characters are separated by a comma maybe mixed of characters or numbers,

2b:Test case
Case: Build a function that would accepts a string and counts the number of words in a string. A word is define as any
     character separated by a comma.
Accepts an empty string and returns None.
     Accepts a string with no space, returns one word
     Accepts a string with spaces, it counts as a word when characters are separated by a comma maybe mixed of characters or numbers,
In order to fulfill the acceptance criteria, a function is build to accept a string that will return the counts of words.
     considering that a word is any character separated by a comma. Numbers and characters are accepted as a string.
"""


def count_words(words):
    words = words.split()                   #removing spaces in the list
    if len(words) == 0:                     #checks if string is empty
        return None
    else:
        return len(words)                   #returning the length of words


