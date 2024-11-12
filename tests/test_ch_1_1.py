from exercise_solutions import ch_1_1

def test_check_if_symmetric():
    assert ch_1_1.check_if_symmetric('frogs') is False
    assert ch_1_1.check_if_symmetric('racecar') is True
    assert ch_1_1.check_if_symmetric('abba') is True
    assert ch_1_1.check_if_symmetric('x') is True
    assert ch_1_1.check_if_symmetric('') is True
    assert ch_1_1.check_if_symmetric('bb') is True
    assert ch_1_1.check_if_symmetric('cx') is False
    assert ch_1_1.check_if_symmetric('!ab123 4 321ba!') is True
    assert ch_1_1.check_if_symmetric(' a a ') is True

def test_convert_to_numbers():
    assert ch_1_1.convert_to_numbers('abc') == [1, 2, 3]
    assert ch_1_1.convert_to_numbers('a cat') == [1, 0, 3, 1, 20]
    assert ch_1_1.convert_to_numbers('') == []

def test_convert_to_letters():
    assert ch_1_1.convert_to_letters([1, 2, 3]) == 'abc'
    assert ch_1_1.convert_to_letters([1, 0, 3, 1, 20]) == 'a cat'
    assert ch_1_1.convert_to_letters([]) == ''
