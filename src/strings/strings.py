def is_unique(string):
    length = len(string)
    if length < 2:
        return True
    if length > 128:
        return False
    lookup = [False]*128

    for char in string:
        if lookup[ord(char)]:
            return False
        lookup[ord(char)] = True

    return True
