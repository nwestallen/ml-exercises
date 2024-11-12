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

def test_get_intersection():
    assert ch_1_1.get_intersection(['a', 'b', 'c'], ['b']) == ['b']
    assert ch_1_1.get_intersection([1, 2, 3], [4, 5, 6]) == []
    assert ch_1_1.get_intersection([1, 'b', 'c'], [1, 'b', 3]) == [1, 'b']
    assert ch_1_1.get_intersection([[1, 2], 0], [[1, 2]]) == [[1, 2]]

def test_get_union():
    assert ch_1_1.get_union(['a', 'b', 'c'], ['b']) == ['a', 'b', 'c']
    assert ch_1_1.get_union([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert ch_1_1.get_union([1, 'b', 'c'], [1, 'b', 3]) == [1, 'b', 'c', 3]
    assert ch_1_1.get_union([[1, 2], 0], [[1, 2]]) == [[1, 2], 0]
