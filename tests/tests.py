import pytest
import the_gallows


the_gallows.WORDS = ['testing']

def test_secret_word():
    word = the_gallows.secret_word()
    assert word == 'testing'

def test_check_len_letter():
    letter = 't'
    assert the_gallows.check_len_letter(letter) == True

@pytest.mark.xfail()
def test_check_len_letter_fail():
    letter = 'aa'
    assert the_gallows.check_len_letter(letter) == True

def test_check_letter():
    word = the_gallows.secret_word()
    letter = 't'
    assert letter in word

def test_check_letter_fail():
    word = the_gallows.secret_word()
    letter = 'a'
    assert letter not in word

def test_string_refactor():
    word = the_gallows.secret_word() # testing
    secret_string = ['_', '_', '_', '_', '_', '_', '_',]
    letter = 't'
    refactor_string = the_gallows.string_refactor(letter, word, secret_string)
    assert ''.join(refactor_string) == 't__t___'

def test_count_decrement(x):
    count = 4
    assert the_gallows.count_decrement(count) == x