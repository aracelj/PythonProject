from U2_2ato2c_count_words import count_words




def test_count_words():
    assert count_words("Minimindomo") == 1
    assert count_words(" ") == None
    assert count_words("") == None
    assert count_words("Peter Piper picked a peck of pickled peppers") == 8
    assert count_words("12 32 cash") == 3
