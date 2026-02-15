#3a Count vowels by Araceli Jakobsson
#Program will return the number of vowels in the string using TDD

"""
#def count_vowels__red(word):
def count_vowels(word):
    return None

"""

#def count_vowels__red(word):               #result red in TDD
#    return None

def count_vowels__green(word):
    count = 0
    word = word.lower()                                      #converting the word input to lowercase
    vowels = "aeiouyåäö"
    for char in word:                                        # checking for the vowels
        if char in vowels:
            count +=1
    return count

def count_vowels__refactor(word):                            # function as count_vowels__green but more refine
    word = word.lower()
    vowels = "aeiouyåäö"
    return len([char for char in word if char in vowels])


