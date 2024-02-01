from lib.check_codeword import *

def test_correct_codeword_is_horse():
    result = check_codeword('Horse')
    assert result == 'Correct! Come in.'

def test_wrong_codeword_no_capital_h():
    result = check_codeword('horse')
    assert result == 'Close, but nope.'

def test_wrong_codeword_anything_else():
    result = check_codeword('graham')
    assert result == 'WRONG!'