from lib.counter import *

def test_counter_at_0():
    counter = Counter()
    assert counter.report() == 'Counted to 0 so far.'

def test_counter_from_0():
    count_one = Counter()
    count_one.add(1)
    result = count_one.report()
    assert result == 'Counted to 1 so far.'

def test_counter_from_10():
    count_two = Counter()
    count_two.add(10)
    result = count_two.report()
    assert result == 'Counted to 10 so far.'

# when we add multiple numbers to the counter, the sum of those numbers is the final count
    
def test_add_multiple_numbers():
    counter = Counter()
    counter.add(5)
    counter.add(10)
    assert counter.report() == 'Counted to 15 so far.'

# def test_counter_from_20():
#     count_three = Counter()
#     count_three.add(15)
#     result = count_three.report()
#     assert result == 'Counted to 20 so far.'