from lib.password_checker import *
import pytest

#Check if it returns true if the password is longer than 8 characters

def test_check_password_is_8_characters_or_longer():
    checker = PasswordChecker()
    password = 'eightcharactersormore'
    assert checker.check(password) == True

    #checks if the passowrd is less than 8 characters and returns invalid password
def test_check_password_is_less_than_8_characters():
    checker = PasswordChecker()
    password = 'short'
    with pytest.raises(Exception) as e:
        checker.check(password)
    error_msg = str(e.value)
    assert error_msg == 'Invalid password, must be 8+ characters.'