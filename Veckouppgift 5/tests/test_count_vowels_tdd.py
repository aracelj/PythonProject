#Program will test using TDD red-green-refactor

from U1_3b_count_vowels_tdd import count_vowels__green, count_vowels__refactor

#to get the red test is when the count_vowels_tdd function is not created yet
#def test_count_vowels__red():
#    assert count_vowels__red("hello") == 1         #TDD red

def test_count_vowels__green():
    assert count_vowels__green("hi") == 1
    assert count_vowels__green("aeiou") == 5
    assert count_vowels__green("HOme") == 2
    assert count_vowels__green("shh") == 0



def test_count_vowels__refactor():
    assert count_vowels__refactor("sju flickor") == 3
    assert count_vowels__refactor("smÖrgÅs") == 2
    assert count_vowels__refactor("shh") == 0


