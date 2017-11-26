from random import shuffle
import pytest

from ..insertion import insertion_sort


def test_raise_exception_with_no_list_as_input():
    with pytest.raises(TypeError):
        insertion_sort()


def test_raise_exception_with_object_as_input():
    with pytest.raises(AssertionError):
        insertion_sort({})


def test_one_element_list_is_ordered():
    input_list = [5]
    expected = [5]
    assert insertion_sort(input_list) == expected


def test_sort():
    size = 10
    to_be_sorted = list(range(size))
    shuffle(to_be_sorted)
    expected = list(range(size))
    assert insertion_sort(to_be_sorted) == expected


def test_sort_string():
    to_be_sorted = ['b', 'c', 'd', 'ee', 'a']
    expected = ['a', 'b', 'c', 'd', 'ee']
    assert insertion_sort(to_be_sorted) == expected


def test_sort_float_and_int():
    to_be_sorted = [1e-5, 1e3, 10, 5.34]
    expected = [1e-5, 5.34, 10, 1e3]
    assert insertion_sort(to_be_sorted) == expected


def test_raise_exception_when_types_are_mixed_within_input_list():
    ''' this test could actually pass with legacy python '''
    to_be_sorted = ['brunet', 1e-5, 1e3, 10, 'adrien', 5.34]
    with pytest.raises(TypeError):
        insertion_sort(to_be_sorted)
