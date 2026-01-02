import pytest
from src.ch01_intro.binary_search import binary_search

def test_binary_search_found():
    my_list = [1, 3, 5, 7, 9]
    assert binary_search(my_list, 3) == 1
    assert binary_search(my_list, 9) == 4

def test_binary_search_not_found():
    my_list = [1, 3, 5, 7, 9]
    assert binary_search(my_list, -1) is None
    assert binary_search(my_list, 10) is None

def test_empty_list():
    assert binary_search([], 3) is None
