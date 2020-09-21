from src.strings import strings


def test_is_unique():
    assert strings.is_unique('')
    assert strings.is_unique('a')
    assert strings.is_unique('abc')
    assert not strings.is_unique('abbccd')
    string = ''.join(chr(i) for i in range(128))
    assert strings.is_unique(string)
    string = ''.join(chr(i % 128) for i in range(129))
    assert not strings.is_unique(string)


def test_is_permutation():
    assert strings.is_permutation3('abbbdbskUJ', 'kUJbbdbbsa')
    assert not strings.is_permutation3('a', '')
    assert not strings.is_permutation3('czZ', 'czz')