from src.strings import strings


def test_empty():
    assert strings.is_unique('')


def test_one():
    assert strings.is_unique('a')


def test_unique():
    assert strings.is_unique('abc')


def test_not_unique():
    assert not strings.is_unique('abbccd')


def test_large_string():
    string = ''.join(chr(i) for i in range(128))
    assert strings.is_unique(string)


def test_too_large_string():
    string = ''.join(chr(i % 128) for i in range(129))
    assert not strings.is_unique(string)
