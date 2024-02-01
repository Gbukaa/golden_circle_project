import pytest
from lib.present import *

# tests if the exception is raised properly when wrap onject is called
def test_checks_wrap_works_correctly():
    present = Present()
    present.wrap('first item')
    with pytest.raises(Exception) as e:
        present.wrap('book')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_checks_unwrap_works_correctly():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_wrap_and_unwrap_sequence():
    present = Present()
    present.wrap('toy')

    wrapped_contents = present.unwrap()

    assert wrapped_contents == 'toy'



# with pytest.raises(Exception) as e: # <-- New code
#         reminder.remind()
#     error_message = str(e.value) # <-- New code
#     assert error_message == 