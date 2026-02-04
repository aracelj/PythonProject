# Exercise 1h Function  by Araceli Jakobsson

"""
Original code:
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
"""


def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:                            #append the item to the list if it is over 4 but less than 8 characters
            found.append(item)
    print(found)                                         #added this line to print what's stored in found list
    return found

average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])

