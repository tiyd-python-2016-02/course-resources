from regex import *


def test_is_lower_alpha():
    assert is_lower_alpha('a')
    assert is_lower_alpha('b')
    assert not is_lower_alpha('')
    assert not is_lower_alpha('A')
    assert not is_lower_alpha('B')


def test_is_upper_alpha():
    assert is_upper_alpha('X')
    assert is_upper_alpha('Y')
    assert not is_upper_alpha('')
    assert not is_upper_alpha('x')
    assert not is_upper_alpha('y')


def test_is_alpha():
    assert is_alpha('xYz')
    assert not is_alpha('')
    assert not is_alpha('a2B')


def test_is_numeric():
    assert is_numeric('1234')
    assert not is_numeric('')
    assert not is_numeric('abcd')


def test_is_alpha_numeric():
    assert is_alpha_numeric('ab12CD45xy67Z')
    assert not is_alpha_numeric('')
    assert not is_alpha_numeric(' ')
    assert not is_alpha_numeric('foo!')


def test_is_alpha_numeric_with_spaces():
    assert is_alpha_numeric_with_spaces('ab12 CD45 xy67 Z')
    assert is_alpha_numeric_with_spaces('foo 1 bar\t 2 baz\n 3 quux 4')
    assert not is_alpha_numeric_with_spaces('foo! bar@ baz$ quux~')
    assert not is_alpha_numeric_with_spaces('')


def test_is_single_letter():
    assert is_single_letter('x')
    assert is_single_letter('Y')
    assert not is_single_letter('')
    assert not is_single_letter('Xx')
    assert not is_single_letter('1')


def test_is_single_digit():
    assert is_single_digit('1')
    assert not is_single_digit('')
    assert not is_single_digit('11')
    assert not is_single_digit('a')


def test_is_eleven_digit_number():
    assert is_eleven_digit_number('12345678901')
    assert not is_eleven_digit_number('')
    assert not is_eleven_digit_number('123456789012')
    assert not is_eleven_digit_number('ABCDEFGHIJK')


def test_has_letter():
    assert has_letter('123a456')
    assert has_letter('123A456')
    assert not has_letter('')
    assert not has_letter('123456')


def test_has_number():
    assert has_number('abc1def')
    assert not has_number('')
    assert not has_number('abcdef')


def test_is_negative_integer():
    assert is_negative_integer('-1234')
    assert not is_negative_integer('')
    assert not is_negative_integer('A')
    assert not is_negative_integer('1234')
    assert not is_negative_integer('-1234A')


def test_is_integer():
    assert is_integer('1234')
    assert is_integer('-1234')
    assert not is_integer('')
    assert not is_integer('12.34')
    assert not is_integer('-12.34')
    assert not is_integer('A')


def test_is_float():
    assert is_float('12.34')
    assert is_float('-12.34')
    assert not is_float('')
    assert not is_float('1234')
    assert not is_float('-1234')
    assert not is_float('A')
    assert not is_float('12.34A')
    assert not is_float('-12.34A')


def test_is_number():
    assert is_number('12.34')
    assert is_number('-12.34')
    assert is_number('1234')
    assert is_number('-1234')
    assert not is_number('')
    assert not is_number('A')
    assert not is_number('1234A')
    assert not is_number('-1234A')


def test_is_fishy():
    assert is_fishy('your facial expression looks fishy today')
    assert not is_fishy('')
    assert not is_fishy('your face smells like a fish today')


def test_is_tweetable():
    assert is_tweetable('A' * 140)
    assert not is_tweetable('')
    assert not is_tweetable('A' * 141)


def test_is_empty():
    assert is_empty('')
    assert not is_empty(' ')


def test_is_whitespace():
    assert is_whitespace(' ')
    assert is_whitespace('\t')
    assert is_whitespace('\n')
    assert is_whitespace(' \t\n')
    assert not is_whitespace('')
    assert not is_whitespace('a')
    assert not is_whitespace(' a')


def test_is_three_or_four_words():
    assert is_three_or_four_words('these are words')
    assert is_three_or_four_words('these are also words')
    assert is_three_or_four_words('  these\tare\twords\ttoo  \n')
    assert not is_three_or_four_words('')
    assert not is_three_or_four_words('word')
    assert not is_three_or_four_words('two words')
    assert not is_three_or_four_words('these are too many words')


def test_extract_words():
    assert extract_words('hello123world') == ['hello', 'world']
    assert extract_words('123!foo!456!bar!') == ['foo', 'bar']
    assert extract_words('123 foo\tbar\nbaz123') == ['foo', 'bar', 'baz']
    assert extract_words('') == []
    assert extract_words('123!') == []


def test_extract_numbers():
    assert extract_numbers('abc123def') == [123]
    assert extract_numbers('45a67') == [45, 67]
    assert extract_numbers('1!2@3#') == [1, 2, 3]
    assert extract_numbers('') == []
    assert extract_numbers('asdf') == []


def test_extract_animals():
    assert extract_animals('the cat in the hat was fat') == ['cat']
    assert extract_animals('the dog and cat chased each other') == ['dog', 'cat']
    assert extract_animals('') == []
    assert extract_animals('there are no animals here') == []


def test_extract_states():
    assert extract_states('here MI are CO a bunch CA of states') == ['MI', 'CO', 'CA']
    assert extract_states('but XZ not LK all CAps ARe states') == []


def test_extract_zips():
    assert extract_zips('only 49418 five digit 27701 zip codes') == ['27701']
    assert extract_zips('but not 532456 six digit 277017 numbers') == []
    assert extract_zips('and not 64321a ones with 27701b characters') == []
