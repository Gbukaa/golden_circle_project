from lib.string_builder import *

# Initially output is an empty string
def test_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ''

#when we add a single string the output is the string

def test_adding_single_string():
    string = StringBuilder()
    string.add('hello')
    result = string.output()
    assert result == 'hello'

#returns the size or length of the single string

def test_adding_a_string_sets_size_to_string():
    string_builder = StringBuilder()
    string_builder.add('hello')
    assert string_builder.size() == 5

#When we add multiple strings the output is those strings concatenated

def test_adding_multiple_strings_outputs_joined_strings():
    string = StringBuilder()
    string.add('hello')
    string.add(' ')
    string.add('world')
    string.add('!')
    result = string.output()
    assert result == 'hello world!'

    #When we add multiple strings the size is the size of the strings added.

def test_adding_multiple_strings_outputs_size_of_joined_strings():
    string = StringBuilder()
    string.add('hello')
    string.add(' ')
    string.add('world')
    string.add('!')
    result = string.size()
    assert result == 12