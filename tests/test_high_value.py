from lib.high_value import *

# this test is to see if the first value is higher
def test_if_first_value_is_higher():
    value = HighValue(2, 1)
    result = value.get_highest()
    assert result == "First value is higher"


# this test is to see if the second value is higher
def test_if_second_value_is_higher():
    value = HighValue(1, 2)
    result = value.get_highest()
    assert result == "Second value is higher"


# this test is to see if both values are equal
def test_if_values_are_equal():
    value = HighValue(2, 2)
    result = value.get_highest()
    assert result == "Values are equal"


# test to see if the first value is selected and increased
def test_if_first_value_is_increased():
    value = HighValue(2, 2)
    value.add(5, 'first')
    result = value.get_highest()
    assert result == 'First value is higher'


# test to see if second value is selected and increased
def test_if_second_value_is_increased():
    value = HighValue(2, 2)
    value.add(5, 'second')
    result = value.get_highest()
    assert result == 'Second value is higher'

#What functionality does the class look like it has? What type are the values being set, added to and compared?
    #class adds two values and checks which one is higher, or if they are equal. 

#What type are the values being set, added to and compared?
    #they are all integers or floats (does actually work with strings!)

#What test(s) can you add to check the two class attributes, set at the time a new object of type HighValue is instantiated?
    #look above at the tests

#What are the three possible outcomes from get_highest() and can you write a separate test for each one?
    #first value is higher, second is higher, values equal. Tests are above.

#What parts of the HighValue object does add() affect? And what are the two different types of ways you could check that? (Hint: there's one method and one non-method way)
    #it affects the first and second values that are input. 
    #You can create a test and assert that it is acting correctly (passing if the correct number is higher)
    #You can also put print statements within the class, instantiate an object and see if the method performed correctly?


