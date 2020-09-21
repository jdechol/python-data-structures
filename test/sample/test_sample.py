from src.sample import sample
import random


def test_quicksort():
    numbers = random.sample(range(1000), 1000)
    actual = sample.quicksort(numbers)
    numbers.sort()
    assert actual == numbers


def test_is_palindrome():
    assert sample.is_palindrome("abcba")
    assert not sample.is_palindrome("ab")
    assert sample.is_palindrome("abba")
    assert sample.is_palindrome("a")