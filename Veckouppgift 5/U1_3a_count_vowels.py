#3a Count vowels by Araceli Jakobsson
#Program will return the number of vowels in the string

"""
Original code:
# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
def count_vowels(word):
    return None

def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0

"""

def count_vowels(word):
    count = 0
    word = word.lower()
    vowels = "aeiouyåäö"
    for char in word:
        if char in vowels:
            count +=1
    return count

def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0

def test_count_vowels():
    assert count_vowels("hi") == 1
    assert count_vowels("aeiou") == 5
    assert count_vowels("Home") == 2
    assert count_vowels("sju ytterligare hus") == 7
    assert count_vowels("smÖrgÅs") == 2
