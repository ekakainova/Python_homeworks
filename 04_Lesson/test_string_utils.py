import pytest
from string_utils import StringUtils

string = StringUtils()


# 1
@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, expected_text', [
    ('hello', 'Hello'),
    ('HELLO world', 'Hello world'),
    ('Hello WORld', 'Hello world')
    ])
def test_string_capitilize_positive(input_text, expected_text):
    assert string.capitilize(input_text) == expected_text


@pytest.mark.negative_test
@pytest.mark.parametrize('input_text, expected_text', [
    ('', ''),
    ('   ', '   '),
    ('/.*', '/.*')
    ])
def test_string_capitilize_negative(input_text, expected_text):
    assert string.capitilize(input_text) == expected_text


# 2
@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, expected_text', [
    (' Hello', 'Hello'),
    ('   Hello', 'Hello'),
    ('1 2 3 ', '1 2 3 ')
    ])
def test_string_trim_positive(input_text, expected_text):
    assert string.trim(input_text) == expected_text


@pytest.mark.negative_test
@pytest.mark.parametrize('input_text, expected_text', [
    ('', ''),
    ('   ', ''),
    ])
def test_string_trim_negative(input_text, expected_text):
    assert string.trim(input_text) == expected_text


# 3
@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, delimeter, expected_text', [
    ('h,e,l,l,o', ',', ['h', 'e', 'l', 'l', 'o']),
    ('1:2:3', ':', ['1', '2', '3']),
    (' .1.k.2.a. ', '.', [' ', '1', 'k', '2', 'a', ' '])
    ])
def test_string_to_list_positive(input_text, delimeter, expected_text):
    assert string.to_list(input_text, delimeter) == expected_text


@pytest.mark.negative_test
@pytest.mark.parametrize('input_text, delimeter, expected_text', [
    ('', ',', []),
    ('   ', ',', []),
    ('   ', ' ', [])
    ])
def test_string_to_list_negative(input_text, delimeter, expected_text):
    assert string.to_list(input_text, delimeter) == expected_text


# 4
@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, symbol, expected_bool', [
    ('Hello', 'l', True),
    ('Hello world', ' ', True),
    ('Hello', 'A', False),
    ('22 april', '2', True)
    ])
def test_string_contains_positive(input_text, symbol, expected_bool):
    assert string.contains(input_text, symbol) == expected_bool


@pytest.mark.negative_test
@pytest.mark.xfail
@pytest.mark.parametrize('input_text, symbol, expected_bool', [
    ('', '', True),
    ('    ', ' ', True),
    ('   ', '', False)  # пустое значение воспринимается программой за пробел и возвращает True
    ])
def test_string_contains_negative(input_text, symbol, expected_bool):
    assert string.contains(input_text, symbol) == expected_bool


# 5
@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, symbol, expected_text', [
    ('Hello', 'l', 'Heo'),
    ('Eka te rina', ' ', 'Ekaterina'),
    ('My23 dream23', '23', 'My dream'),
    ('Hel  lo wor  ld', '  ', 'Hello world')
    ])
def test_string_delete_symbol_positive(input_text, symbol, expected_text):
    assert string.delete_symbol(input_text, symbol) == expected_text


@pytest.mark.negative_test
@pytest.mark.parametrize('input_text, symbol, expected_text', [
    ('   ', ' ', ''),
    ('', '', ''),
    ('hello', 'H', 'hello')
    ])
def test_string_delete_symbol_negative(input_text, symbol, expected_text):
    assert string.delete_symbol(input_text, symbol) == expected_text


# 6
@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, symbol, expected_text', [
    ('Hello', 'H', True),
    ('Hello', 'h', False),
    ('Hello', 'Hel', True),
    (' Hello', ' ', True),
    ('22 April', '22', True)
    ])
def test_string_starts_with_positive(input_text, symbol, expected_text):
    assert string.starts_with(input_text, symbol) == expected_text


@pytest.mark.negative_test
@pytest.mark.xfail
@pytest.mark.parametrize('input_text, symbol, expected_text', [
    ('', '', True),
    ('   ', ' ', True),
    (' Mo', '', False)  # пустое значение воспринимается программой за пробел и возвращает True
    ])
def test_string_starts_with_negative(input_text, symbol, expected_text):
    assert string.starts_with(input_text, symbol) == expected_text


# 7
@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, symbol, expected_text', [
    ('Hello', 'o', True),
    ('Hello', 'O', False),
    ('Hello', 'llo', True),
    ('Hello ', ' ', True),
    ('April 1990', '90', True)
    ])
def test_string_end_with_positive(input_text, symbol, expected_text):
    assert string.end_with(input_text, symbol) == expected_text


@pytest.mark.negative_test
@pytest.mark.xfail
@pytest.mark.parametrize('input_text, symbol, expected_text', [
    ('', '', True),
    ('   ', ' ', True),
    ('Mo ', '', False)  # пустое значение воспринимается программой за пробел и возвращает True
    ])
def test_string_end_with_negative(input_text, symbol, expected_text):
    assert string.end_with(input_text, symbol) == expected_text


# 8
@pytest.mark.positive_test
@pytest.mark.parametrize('input_text, expected_text', [
    ('', True),
    ('   ', True),
    (' . ', False),
    ('Hello', False),
    ('123', False)
    ])
def test_string_is_empty_positive(input_text, expected_text):
    assert string.is_empty(input_text) == expected_text


@pytest.mark.negative_test
@pytest.mark.parametrize('input_text', [
    (123),
    (None)
    ])
def test_string_is_empty_negative(input_text):
    with pytest.raises(AttributeError):
        string.is_empty(input_text)


# 9
@pytest.mark.positive_test
@pytest.mark.parametrize('input_list, joiner, expected_text', [
    ([1, 2, 3, 4, 5], ', ', '1, 2, 3, 4, 5'),
    (['He', 'l', 'lo'], ' ', 'He l lo'),
    (['Anna', 'Maria'], '-', 'Anna-Maria'),
    ([1, 'A', 2, 'n', 3, 'n', 4, 'a'], '', '1A2n3n4a')
    ])
def test_list_to_string_positive(input_list, joiner, expected_text):
    assert string.list_to_string(input_list, joiner) == expected_text


@pytest.mark.negative_test
@pytest.mark.parametrize('input_list, joiner, expected_text', [
    ([], ', ', ''),
    (['    '], ', ', '    '),
    ])
def test_list_to_string_negative(input_list, joiner, expected_text):
    assert string.list_to_string(input_list, joiner) == expected_text
