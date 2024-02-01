from lib.gratitudes import *

# adds a gratitude to the list of gratitudes

def test_adds_gratitude_to_list_when_called_checks_formatting():
    gratitude = Gratitudes()
    gratitude.add('cheese')
    assert gratitude.format() == 'Be grateful for: cheese'

    # test that the list is being appended to

def test_adds_gratitude_to_list_checks_append_is_working():
    gratitude = Gratitudes()
    gratitude.add('eggs')
    assert gratitude.gratitudes == ['eggs']

