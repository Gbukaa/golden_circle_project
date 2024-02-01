from lib.report_length import *

def test_report_length_of_a_string():
    result = report_length('this string is 33 characters long')
    assert result == 'This string was 33 characters long.'

def test_report_length_of_goop_string():
    result = report_length('goop')
    assert result == 'This string was 4 characters long.'

def test_report_length_of_sausage_string():
    result = report_length('sausages')
    assert result == 'This string was 8 characters long.'

def test_report_length_of_short_string():
    result = report_length('A')
    assert result == 'This string was 1 characters long.'