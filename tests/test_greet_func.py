from lib.greet import *

def test_greet_function_returns_name():
    result = greet('Bob')
    assert result == "Hello, Bob!"

